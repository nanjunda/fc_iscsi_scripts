import os
import sys

#
# Generate medusa scripts for various buffer sizes, Q-Depths and read-write operations in terms of percentage
# Buffer sizes: 512b, 1k, 2k, 4k, 8k, 16k, 32k, 54k, 128k, 256k, 512k, 1m (both read and write buffers)
# Q-Depths : 1, 2, 4, 8, 16, 32, 64, 128, 256, 512
# Read-Write percentage combinations: 100% Read/0% Write, 70% Read/30% Write, 50% Read/50% Write, 0% Read/100% Write
#
# command line sample:
# maim --perf-mode -tp --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s
#       --full-device -x0u -%100:r100@512b,w0@512b,x0,f100 -Q64 -d120
# maim --perf-mode -tp --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s
#       --full-device -x0u -%100:r0@512b,w100@512b,x0,f100 -Q64 -d120
# maim --perf-mode -tp --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s
#       --full-device -x0u -%100:r50@512b,w50@512b,x0,f100 -Q64 -d120
# maim --perf-mode -tp --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s
#       --full-device -x0u -%100:r70@512b,w30@512b,x0,f100 -Q64 -d120
# Output the results in a file called TimeStamp_QXXX_RXXX_BXXX
#
# How to use this script:
#
# python generateMedusaScripts.py iSCSI Phase2 Normal ../config/targets.dat 100 0 240 12p | grep -v "R0_W100" > X100_NO_R0_W100
# the above command will generate command line (for iSCSI, Normal, labelled as Phase 2 for 100% random IO, 0% sequential IO 
# each command will run for 240 secs using 12 threads - refer to Medusa maim command option for -t.
# in the output grep all the command lines - maim, two mv - *except* 100% writes since we want to do writes with 100% sequential to 
# simulate writing database log files.
#
# python generateMedusaScripts.py iSCSI Phase2 Normal ../config/targets.dat 0 100 240 12p | grep  "R0_W100" > F100__SEQUENTIAL_R0_W100
# above line is similar to what is explained for previous example. But, here we are capturing *only* 100% writes with 100% sequential IO 
# *no* random IO
#

#
# generate result output file name in the form TimeStamp_QXXX_RXXX_BXXX and return the file name to called function
# "Run*" file name is for perfmon file in C:/Perflog/Admin/FC_iSCSI
#
def  resultOutputFile(q, r, w, b) :
    # time stamp in shell variable TS; see below
    ts = '${TS}'
    hn = "`uname -n`"
    pf = "Run*"
    
    csvInFile = hn + ".csv"
    logInFile = hn + ".log"
    prfInFile = hn + ".prf"   
    cpuInFile = pf + ".csv"

    output_file_name_prefix = ts + "_Q" + q + "_R" + r + "_W" + w + "_B" + b + "_X" + randomPercent + "_F" + seqPercent + "_D" + runTime + "_" + protocol + "_" + phase + "_" + testType + "_" + hn

    csvOutFile = output_file_name_prefix + ".csv"
    logOutFile = output_file_name_prefix + ".log"
    prfOutFile = output_file_name_prefix + ".prf"
    cmdOutFile = output_file_name_prefix + ".out"
    cpuOutFile = output_file_name_prefix + "_CPU" + ".csv"
    
    tsVar = "TS=`date +%y%m%d%H%M%S`"
    csvMv = "mv " + csvInFile + "  " + csvOutFile
    logMv = "mv " + logInFile + "  " + logOutFile
    prfMv = "mv " + prfInFile + "  " + prfOutFile
    cpuMv = "mv " + cpuInFile + "  " + cpuOutFile

    
    #outFiles is list of strings. As name suggests element 0 is file name for cmd output, element 1 is rename (mv) csv file, log file and prf file
    outFiles = [tsVar, cmdOutFile, csvMv, logMv, prfMv, cpuMv]
    return (outFiles)               
                
#
# convert number to bytes bs (int) to kb (string)
#
def bytesToKb(bs) :

    kb = []
    
    if bs < 1024:
        kb = str(bs) + "b"
    elif bs < 1048576:
        kb = str(int(bs/1024)) + "k"
    else :
        kb = str(int(bs/(1024*1024))) + "m"
    return(str(kb))

#
# form individual command line for maim
#             
def generate_command_line(q, r, w, b) :
    
    command_line_start = "maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u"
    command_line_end = " > "
    
    bs = bytesToKb(b)
    outFiles = resultOutputFile(q, r, w, bs)
    command_line_middle =  " -t" + threads + " -b" + bs + " -%100:r" + r + ",w" + w + ",x" + randomPercent + ",f" + seqPercent + " -Q" + q + " -d" + runTime + " -M600" + " -f" + targets
    cmdL = command_line_start + command_line_middle + command_line_end + outFiles[1]
    cl = [outFiles[0], cmdL, outFiles[2], outFiles[3], outFiles[4], outFiles[5]]
    return (cl)


#
# Generate medusa command  line for maim similar to mentioned above
#
def genMedusaScript() :

    qdepth_list = [8, 16, 32, 64, 128]
    buffer_size_list = [512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]
    rd_list = [100, 70, 50, 0]
    
    for qd in qdepth_list:
        for rd in rd_list:
            for bs in buffer_size_list:
                qd_string = str(qd)
                rd_string = str(rd)
                wr_string = str(100-rd)            
                command_line = generate_command_line(qd_string, rd_string, wr_string, bs)               

                """
                print(logman start line)
                """
                print("logman_start")
                """
                logman started
                """

                print(command_line[0])
                print(command_line[1])
                print(command_line[2])
                print(command_line[3])
                print(command_line[4])

                """
                print(logman stopped line)
                """
                print("logman_stop")
                """
                logman stopped
                and them rename Run*.csv file
                """

                print(command_line[5])
                
#
# main function 
# argument 1 - protocol:  FC or iSCSI
# argument 2 - phase : Phase1, Phase2, etc (test phases based on test configurations)
# argument 3 - testType: NORMAL, CONGESTION, DISRUPTION, etc.
# argument 4 - targets file path
# argument 5 - random IO percent
# argument 6 - sequential IO  percent
# argument 7 - run time
# argument 8 - number of threads (p is added by default at the end e.g. -t12p)
#

argc = len(sys.argv)
if argc < 8 :
    print("<cmd> protocol phase test type, targets file, random percent, sequential percent, threads")
else :
    protocol = sys.argv[1]
    phase = sys.argv[2]
    testType = sys.argv[3]
    targets = sys.argv[4]
    randomPercent = sys.argv[5]
    seqPercent = sys.argv[6]
    runTime=sys.argv[7]
    threads = sys.argv[8]
    genMedusaScript()

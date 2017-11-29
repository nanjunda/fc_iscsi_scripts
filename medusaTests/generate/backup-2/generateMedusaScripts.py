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


def result_output_file(q, r, w, b):
    # time stamp in shell variable TS; see below
    ts = '${TS}'
    hn = "`uname -n`"
    pf = "Run*"

    csv_in_file = hn + ".csv"
    log_in_file = hn + ".log"
    prf_in_file = hn + ".prf"
    cpu_in_file = pf + ".csv"

    output_file_name_prefix = ts + "_Q" + q + "_R" + r + "_W" + w + "_B" + b + "_X" + random_percent + "_F" + seq_percent + "_D" + run_time + "_" + protocol + "_" + phase + "_" + test_type + "_" + hn

    csv_out_file = output_file_name_prefix + ".csv"
    log_out_file = output_file_name_prefix + ".log"
    prf_out_file = output_file_name_prefix + ".prf"
    cmd_out_file = output_file_name_prefix + ".out"
    cpu_out_file = output_file_name_prefix + "_CPU" + ".csv"

    ts_var = "TS=`date +%y%m%d%H%M%S`"
    csv_mv = "mv " + csv_in_file + "  " + csv_out_file
    log_mv = "mv " + log_in_file + "  " + log_out_file
    prf_mv = "mv " + prf_in_file + "  " + prf_out_file
    cpu_mv = "mv " + cpu_in_file + "  " + cpu_out_file

#   out_files is list of strings. As name suggests element 0 is file name for cmd output, element 1 is rename (mv) csv file, log file and prf file
    out_files = [ts_var, cmd_out_file, csv_mv, log_mv, prf_mv, cpu_mv]
    return (out_files)

#
# convert number to bytes bs (int) to kb (string)
#

def bytes_to_kb(bs):
    kb = []

    if bs < 1024:
        kb = str(bs) + "b"
    elif bs < 1048576:
        kb = str(int(bs/1024)) + "k"
    else:
        kb = str(int(bs/(1024*1024))) + "m"
    return(str(kb))

#
# convert number to bytes bs (int) to kb (string)
#

def kb_to_bytes(siz):
    b = 0
    l = len(siz)
    if ("k" in siz):
        b=int(siz[:l-1])*1024
    elif ("m" in siz):
        b = int(siz[:l-1])*1024*1024 
    elif ("b" in siz):
        b = int(siz[:l-1]) 
    return(b)




# form individual command line for maim
#
def generate_command_line(q, r, w, b):

    command_line_start = "maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u"
    command_line_end = " > "

    bs = bytes_to_kb(b)
    out_files = result_output_file(q, r, w, bs)
    command_line_middle = " -t" + threads + " -b" + bs + " -%100:r" + r + ",w" + w + ",x" + random_percent + ",f" + seq_percent + " -Q" + q + " -d" + run_time + " -M600" + " -f" + targets
    cmdL = command_line_start + command_line_middle + command_line_end + out_files[1]
    cl = [out_files[0], cmdL, out_files[2], out_files[3], out_files[4], out_files[5]]
    return (cl)


#
# parse ranges - qdepth, buffer size, read percent
#

def parse_ranges():
    qstart, qend = qdepth_range.split('-')
    buf_start, buf_end = bufsiz_range.split('-')


    m = int(qstart)
    n = int(qend)

    while (m < 2*n):
        qdepth_list.append(m)
        m = 2*m
    m = kb_to_bytes(buf_start)
    n = kb_to_bytes(buf_end)
    while (m < 2*n):
        buffer_size_list.append(m)
        m = 2*m
    l = len(read_percent_range.split('-'))
    i = 5 - l
    ss = read_percent_range
    while (i > 0):
        ss = ss + "-XX"
        i -= 1
    rd100, rd70, rd50, rd30, rd0 = ss.split('-')
    if ("XX" not in rd100):
        rd_list.append(int(rd100))
    if ("XX" not in rd70):
        rd_list.append(int(rd70))
    if ("XX" not in rd50):
        rd_list.append(int(rd50))
    if ("XX" not in rd30):
        rd_list.append(int(rd30))
    if ("XX" not in rd0):
        rd_list.append(int(rd0))

#
# Generate medusa command  line for maim similar to mentioned above
#
def gen_medusa_script() :

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
# argument 3 - test_type: NORMAL, CONGESTION, DISRUPTION, etc.
# argument 4 - targets file path
# argument 5 - random IO percent
# argument 6 - sequential IO  percent
# argument 7 - run time
# argument 8 - number of threads (p is added by default at the end e.g. -t12p)
# argement 9 - qdepth range
# argement 10 - buffer size range
# argument 11 - read percent (implies write percent 100 - read percent)
#

qdepth_list = []
buffer_size_list = []
rd_list = []

argc = len(sys.argv)
if argc < 8:
    print("<cmd> protocol phase test type, targets file, random percent, sequential percent, threads")
else :
    protocol = sys.argv[1]
    phase = sys.argv[2]
    test_type = sys.argv[3]
    targets = sys.argv[4]
    random_percent = sys.argv[5]
    seq_percent = sys.argv[6]
    run_time=sys.argv[7]
    threads = sys.argv[8]
    qdepth_range = sys.argv[9]
    bufsiz_range = sys.argv[10]
    read_percent_range = sys.argv[11]
    parse_ranges()
    gen_medusa_script()

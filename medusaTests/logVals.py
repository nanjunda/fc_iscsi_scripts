#
# Python script to calculate log values for the numbers in total summary csv file
# this gives better perspective when these values are put in a chart to see rate of change
# as one plots buffer size against IOPS, latency(IO Completion Time) and throughput (MB/S)
#
import csv
import sys
import time
import numpy as np

from math import sqrt

file_name = sys.argv[1]

sys.stdout.write("Time Stamp, I/F, Phase, xVal, fVal, Size, Q-Depth, Read, Write, SD:IOPS, SD:MB/S, SD:IO Completion Time, MN:IOPS, MN:MB/S, MN:IO Completion Time, 100th:IOPS, 100th:MB/S, 100th:IO Completion Time, Tag")

print (", SD:IOPS_L, SD:MB/S_L, SD:IO Completion Time_L, MN:IOPS_L, MN:MB/S_L, MN:IO Completion Time_L, 100th:IOPS_L, 100th:MB/S_L, 100th:IO Completion Time_L")
with open(file_name) as csvfile:


    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    for row in readCSV :
       i = 0
       while (i < len(row)):
          sys.stdout.write(str(row[i]))
          sys.stdout.write(", ")
          i = i + 1
       logRow9 = []
       logRow10 = []
       logRow11 = []
       logRow12 = []
       logRow13 = []
       logRow14 = []
       logRow15 = []
       logRow16 = []
       logRow17 = []
       logRow9  = np.log(float(row[9]))
       logRow10 = np.log(float(row[10]))
       logRow11 = np.log(float(row[11]))
       logRow12 = np.log(float(row[12]))
       logRow13 = np.log(float(row[13]))
       logRow14 = np.log(float(row[14]))
       logRow15 = np.log(float(row[15]))
       logRow16 = np.log(float(row[16]))
       logRow17 = np.log(float(row[17]))
       print ("%.4f, %.4f, %.8f, %.4f, %.4f, %.8f, %.4f, %.4f, %.8f" % (logRow9, logRow10, logRow11, logRow12, logRow13, logRow14, logRow15, logRow16, logRow17, ))

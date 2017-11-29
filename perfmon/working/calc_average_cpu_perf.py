#
# Python script to calculate average of CPU perfmon data in  csv file
#
import csv
import sys
import time
import numpy as np

from math import sqrt

file_name = sys.argv[1]

"""
sys.stdout.write("Time,CPU % Idle Time,CPU % Intr Time,CPU % Privileged Time,CPU % Proc Time,CPU % User Time")
"""
print("Time,CPU % Idle Time,CPU % Intr Time,CPU % Privileged Time,CPU % Proc Time,CPU % User Time")

with open(file_name) as csvfile:


    time_stamp = "Average"
    av_cpu_idle_time = 0.0
    av_cpu_intr_time = 0.0
    av_cpu_priv_time = 0.0
    av_cpu_proc_time = 0.0
    av_cpu_user_time = 0.0

    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    next(readCSV)
    no_rows = 0
    for row in readCSV :
       print ("%s, %s, %s, %s, %s, %s" %  (str(row[0]), str(row[119]), str(row[144]), str(row[169]), str(row[194]), str(row[219])))
       av_cpu_idle_time  += float(row[119])
       av_cpu_intr_time  += float(row[144])
       av_cpu_priv_time  += float(row[169])
       av_cpu_proc_time  += float(row[194])
       av_cpu_user_time  += float(row[219])
       no_rows += 1
    av_cpu_idle_time = av_cpu_idle_time/no_rows
    av_cpu_intr_time = av_cpu_intr_time/no_rows
    av_cpu_priv_time = av_cpu_priv_time/no_rows
    av_cpu_proc_time = av_cpu_proc_time/no_rows
    av_cpu_user_time = av_cpu_user_time/no_rows
    print ("%s, %.10f, %.10f, %.10f, %.10f, %.10f" % (time_stamp, av_cpu_idle_time, av_cpu_intr_time, av_cpu_priv_time, av_cpu_proc_time, av_cpu_user_time ))

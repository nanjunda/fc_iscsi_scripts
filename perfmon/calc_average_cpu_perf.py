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

    prev_cpu_idle_time = 0.0
    prev_cpu_intr_time = 0.0
    prev_cpu_priv_time = 0.0
    prev_cpu_proc_time = 0.0
    prev_cpu_user_time = 0.0

    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    next(readCSV)
    no_rows = 0
#
# calculate the average from each _CPU.csv file which is output of logman (Windows Perfmon). Sometimes, the output has
# blanks and need to handle the blanks. If there is blank the reading, the algorigham will take previous reading so that
# average won't get affected drastically
#
    for row in readCSV :
       print ("%s, %s, %s, %s, %s, %s" %  (str(row[0]), str(row[101]), str(row[126]), str(row[151]), str(row[176]), str(row[201])))
       try:
        av_cpu_idle_time  += float(row[101])
        prev_cpu_idle_time = float(row[101])
       except ValueError:
        av_cpu_idle_time  += prev_cpu_idle_time
       try:
        av_cpu_intr_time  += float(row[126])
        prev_cpu_intr_time  = float(row[126])
       except ValueError:
        av_cpu_intr_time  += prev_cpu_intr_time 
       try:
        av_cpu_priv_time  += float(row[151])
        prev_cpu_priv_time  = float(row[151])
       except ValueError:
        av_cpu_priv_time  += prev_cpu_priv_time
       try:
        av_cpu_proc_time  += float(row[176])
        prev_cpu_proc_time  = float(row[176])
       except ValueError:
        av_cpu_proc_time  += prev_cpu_proc_time
       try:
        av_cpu_user_time  += float(row[201])
        prev_cpu_user_time  = float(row[201])
       except ValueError:
        av_cpu_user_time  += prev_cpu_user_time
       no_rows += 1
    if (no_rows > 0):
        av_cpu_idle_time = av_cpu_idle_time/no_rows
        av_cpu_intr_time = av_cpu_intr_time/no_rows
        av_cpu_priv_time = av_cpu_priv_time/no_rows
        av_cpu_proc_time = av_cpu_proc_time/no_rows
        av_cpu_user_time = av_cpu_user_time/no_rows
        print ("%s, %.10f, %.10f, %.10f, %.10f, %.10f" % (time_stamp, av_cpu_idle_time, av_cpu_intr_time, av_cpu_priv_time, av_cpu_proc_time, av_cpu_user_time ))

#
# update - change the columns from Average IOPS(column4) to Current IOPS (column3) and average MB/S(column8) to current MB/s(column7)
# column index starts from 0 
#

#
# Python script to calculate std. deviation and mean
#
import csv
import sys
import time
import numpy as np

from math import sqrt

#
# Calculate mean
#
def mean(lst):
    """calculates mean"""
    np_array = np.array(lst)
    return (np_array.mean(dtype=np.float64))

#
# find the outlier in the data by identifying data that is outside 
# mean + 2*SD and mean - 2*SD, then calcuate mean of all the data that are not
# outliers. 
# first calculate standard deviation, find all the number that are not ourliers, and then find mean
#
def stddev(lst):
    """calculates standard deviation"""

    std_lst = []

    np_array = np.array(lst)
    sigma2_plus = np_array.mean(dtype=np.float64) + (2*(np_array.std(dtype=np.float64)))
    sigma2_minus = np_array.mean(dtype=np.float64) - (2*(np_array.std(dtype=np.float64)))

# find outliers - anything above mean + 2 sigma or mean - 2 sigma is outlier
    i = 0
    while (i < len(lst)) :
       if (lst[i] <= sigma2_plus and lst[i] >= sigma2_minus) :
          std_lst.append(lst[i])
       i = i + 1
    
    np_std_array = np.array(std_lst)
    return (np_std_array.mean(dtype=np.float64))

#
# Get 100rh entry (Marcus method :-) )
#
def get100th(lst):
    """Get 100th entry"""
    if (len(lst) > 100):
       val100 = lst[99]
    else:
       val100 = lst[int(round(len(lst)/2))]
    return(val100)




def subStrFind(str, substr_list):
    fnd=-1
    for s in substr_list:
       if ((str.find(s)) != -1):
          fnd = s
          break
       else:
          continue
    return (fnd)



def bufsize(str):
    """find the buf size using file name"""

    bufsize_array = ["B512b", "B1k", "B2k", "B4k", "B8k", "B16k", "B32k", "B64k", "B128k", "B256k", "B512k", "B1m"]
    bufsize_int = [512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]
 
    bufsize=subStrFind(str, bufsize_array)
    bufsize_index = bufsize_array.index(bufsize)
    return(bufsize_int[bufsize_index])


def qdepth(str):

    qdepth_array = ["Q1_", "Q2_", "Q4_", "Q8_", "Q16_", "Q32_", "Q64_", "Q128_", "Q256_", "Q512_"]

    
    qdep=subStrFind(str, qdepth_array)
    if (qdep != -1):
       dep = qdep[1:(len(qdep)-1)]
    else:
       dep = qdep
    return(int(dep))


def rdwr(str):
    """find the read vs write using file name"""

    rd_array = ["R100", "R70", "R50", "R0"]

    rd=subStrFind(str, rd_array)
    if (rd != -1):
       rdwr = rd[1:(len(rd))]
    else:
       rdwr = rd
    return(int(rdwr))



file_name = sys.argv[1]
size = bufsize(file_name)
qd = qdepth(file_name)
rds = rdwr(file_name)
wrs = 100 - rds

print (file_name, size, qd, rds, wrs)
time.sleep(2)

with open(file_name) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    column3 = []
    column7 = []
    column11 = []
    for row in readCSV:
        column3.append(float(row[3]))
        column7.append(float(row[7]))
        column11.append(float(row[11]))
    print ("Size, Q-Depth, Read, Write, SD:IOPS, SD:MB/S, SD:IO Completion Time, MN:IOPS, MN:MB/S, MN:IO Completion Time, 100th:IOPS, 100th:MB/S, 100th:IO Completion Time")
    print ("%d, %d, %d, %d, %.4f, %.4f, %.8f, %.4f, %.4f, %.8f, %.4f, %.4f, %.8f" % (size, qd, rds, wrs, stddev(column3), stddev(column7), stddev(column11), mean(column3), mean(column7), mean(column11), get100th(column3), get100th(column7), get100th(column11), ))

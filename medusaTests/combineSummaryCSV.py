#
# Python script to append iSCSI total summary csv file in terms of columns
# this facilitates to put FC and iSCSI data columns side by side to compare
# first argument is a file with columnar join of FC and iSCSI total summary CSV files
# second argument is the new file that changes header row and removed unnecessary columns
# iSCSI total summary file.
# to get the file given in first argument do the following:
#  + Add "," at the end of each row in FC Total summary file (using sed)
#  + paste <above FC total summary file> <iSCSI total summary file>
#  + Fix CRLF problem using "dos2unix" command (d2u) on pasted summary file
#  + python combineSummaryCSV.py <pasted file> <new file>
# Assumption: Both FC and iSCSI tests with the exact same parameters
# python combineSummaryCSV <FC+iSCSI pasted Summary File> <new File>
# use the shell script - combinedTotalSummary.sh (TBD)
#
import csv
import sys
import time

file_name1 = sys.argv[1]
file_name2 = sys.argv[2]

header_row = ["Time Stamp", "I/F", "Phase", "xVal", "fVal", "Size", "Q-Depth", "Read", "Write", "FC_SD:IOPS", "FC_SD:MB/S", "FC_SD:IO Completion Time", "FC_MN:IOPS", "FC_MN:MB/S", "FC_MN:IO Completion Time", "FC_100th:IOPS", "FC_100th:MB/S", "FC_100th:IO Completion Time", "iSCSI_SD:IOPS", "iSCSI_SD:MB/S", "iSCSI_SD:IO Completion Time", "iSCSI_MN:IOPS", "iSCSI_MN:MB/S", "iSCSI_MN:IO Completion Time", "iSCSI_100th:IOPS", "iSCSI_100th:MB/S", "iSCSI_100th:IO Completion Time", "tag"]

with open(file_name2, 'w') as csvfile2:
	writeCSV2 = csv.writer(csvfile2, delimiter=',')
	writeCSV2.writerow(header_row)
	with open(file_name1) as csvfile1:
		readCSV1 = csv.reader(csvfile1, delimiter=',')
		next(readCSV1)
		for row1 in readCSV1 :
			row = []
			l = len(row1)
			i = 0
			while (i < l):
				print (i)
				if (i < 18 or i > 27):
					row.append(str(row1[i]))
				i = i + 1
			writeCSV2.writerow(row)

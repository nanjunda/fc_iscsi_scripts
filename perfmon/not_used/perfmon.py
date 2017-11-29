import sys
import csv
import os


csv_filename = sys.argv[1]
with open(csv_filename) as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print ("%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" %  (str(row[0]), str(row[119]), str(row[144]), str(row[169]), str(row[194]), str(row[219]), str(row[220]), str(row[221]), str(row[234]), str(row[247]), str(row[248]), str(row[261])))

import csv
import os

def tagDir(dir, tag):
	test_type_file = dir + "/" + ".testType"
	print (test_type_file) 
	with open (test_type_file, 'w') as f:
		f.write(tag)
		f.close()

with open('iSCSI_FC_csvFileList.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	next(readCSV)
	for row in readCSV:
		dir = str(row[0])
		test_type = str(row[2])
		if (os.path.exists(dir)):
			tagDir(dir, test_type)
		else:
			continue

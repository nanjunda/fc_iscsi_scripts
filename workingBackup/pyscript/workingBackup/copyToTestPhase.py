#
# find the interface or tech (FC or iSCSI), test type (Normal or Congestion), phase (phase 1 - single switch or phase 2 - fabric)
# tag the above information in each directory in a file called .testType
#
import csv
import os

def tagDir(dir, tag):
	test_type_file = dir + "/" + ".testType"
#	print (test_type_file) 
	with open (test_type_file, 'w') as f:
		f.write(tag)
		f.close()

def subStrFind(str, substr_list):
    fnd=-1
    for s in substr_list:
       if ((str.find(s)) != -1):
          fnd = s
          break
       else:
          continue
    return (fnd)


def findPhase(str):

    """find phase of the tests using file iSCSI_FC_csvFileList.csv in the directory processedFiles """

    phase_array = ["iSCSI_Phase_1", "iSCSI_Phase_2", "FC_Phase_1", "FC_Phase_2"]

    phase=subStrFind(str, phase_array)
    return(phase)



with open('iSCSI_FC_csvFileList.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	next(readCSV)
	for row in readCSV:
		dir = str(row[0])
		file_name=str(row[1])
		test_type = str(row[2])
		phase_tech = findPhase(file_name)
		if (phase_tech == "iSCSI_Phase_1"):
			phase = "Phase_1"
			tech = "iSCSI"
		elif (phase_tech == "iSCSI_Phase_2"):
			phase = "Phase_2"
			tech = "iSCSI"
		elif (phase_tech == "FC_Phase_1"):
			phase = "Phase_1"
			tech = "FC"
		elif (phase_tech == "FC_Phase_2"):
			phase = "Phase_2"
			tech = "FC"
		else:
			phase = "None"
			tech = "None"
		if (os.path.exists(dir)):
			tags = tech + ":" + phase + ":" + test_type 
			tagDir(dir, tags)
#			print (dir, tags)
		else:
			continue

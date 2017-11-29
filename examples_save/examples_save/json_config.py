import sys
import json
from pprint import pprint

configFile = sys.argv[1]

with open(configFile) as data_file:    
    data = json.load(data_file)
pprint(data)
print(data["Switches"][0]["switchName"])
arrayLen = len(data["Switches"][0]["flows"])
i = 0
while (i<arrayLen):
	print(data["Switches"][0]["flows"][i])
	i = i+1

arrayLen = len(data["SwitchAttributes"]["workFlow"])
i=0
while (i<arrayLen):
	print(data["SwitchAttributes"]["workFlow"][i])
	i = i+1
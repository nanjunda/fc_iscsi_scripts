#
# this script reads swich configuration in JSON and converts to Python object called BrocadeSANSwitch
# defined in the file "sanSwitchTestOperations.py. The JSON based configuration file used for this script
# available in this directory - switchConfig.json
# once the json based configuration is read, this gets converted into 'namedTuple' which makes reading
# switch configuration is much easier.
# this script takes "configuration file name" as the argument. Make sure that you follow the JSON syntax 
# properly as JSON has very strict syntax check including 'comma', bracket etc.
# Important Note: this script is still work-in-progress. I am yet to convert namedTuple to BrocadeSANSwitch

import sys
import json
from pprint import pprint
from collections import namedtuple

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())

def load_data(file_name):
  with open(file_name, 'r') as file_data:
    return file_data.read().replace('\n', '')
	
def json2obj(file_name): return json.loads(load_data(file_name), object_hook=_json_object_hook)

configFile = sys.argv[1]

san = json2obj(configFile)
num_switches = len(san.Switches)
i=0
while (i<num_switches):
	print (san.Switches[i].switchName)
	print (san.Switches[i].mgmtIP)
	print (san.Switches[i].userName)
	print (san.Switches[i].userPassword)
	num_flows = len(san.Switches[i].flows)
	j=0
	while (j<num_flows):
		print (san.Switches[i].flows[j].flowName)
		j += 1
	i += 1

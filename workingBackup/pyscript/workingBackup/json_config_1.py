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

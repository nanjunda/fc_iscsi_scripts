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
import paramiko
import json
from pprint import pprint
from collections import namedtuple

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())

def load_data(file_name):
  with open(file_name, 'r') as file_data:
    return file_data.read().replace('\n', '')
	
def json2obj(file_name): return json.loads(load_data(file_name), object_hook=_json_object_hook)

#
# Brocade Switch Class definition
#

class BrocadeSANSwitch:

    """
    Class:
    Brocade SAN Switch 
    Attributes:
    mgmt_ip: management IP address
    user_name: user name to login
    user_password: user password to login
    """

    flows = []


    def __init__(self, switch_name, mgmt_ip, user_name, user_password, flow_names, command):
        self.switch_name = switch_name
        self.mgmt_ip = mgmt_ip
        self.user_name = user_name
        self.user_password = user_password
        self.flow_names = flow_names
        self.ssh_client_handle =  paramiko.SSHClient()
        self.command = command
        self._create_flow_objects()


    def ssh_to_switch(self):
        self.ssh_client_handle.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client_handle.connect(self.mgmt_ip, username=self.user_name, password=self.user_password)


    def execute_cmd(self):
        num_cmd_strings = len(self.command)
        j=0
        while (j<num_cmd_strings):
            cmd = self.command[j]
            stdin, stdout, stderr = self.ssh_client_handle.exec_command(cmd)
            print(stdout.read().strip())
            j += 1

    def _create_flow_objects(self):
        num_flow_names = len(self.flow_names)
        j=0
        while (j<num_flow_names):
            fl = BrocadeSANFlow(self.flow_names[j])
            self.flows.append(fl)
            j += 1

#
# this python script defines Brocade SAN Flow as an object
# with flow attributes and methods related to flow
#

class BrocadeSANFlow:

    """
    Class:
    Brocade SAN Flow 
    Attributes:
    """


    def __init__(self, flow_name):
        self.flow_name = flow_name

    def show_flow(self):
        cmd = "flow --show " + flow_name
        self.san_switch.execute_cmd(cmd)

    def execute_cmd(self):
        stdin, stdout, stderr = self.ssh_client_handle.exec_command(self.command)
        print(stdout.read().strip())


configFile = sys.argv[1]
san_switch = []
flownames = []
cmd_string = []

san = json2obj(configFile)
num_switches = len(san.Switches)
i=0
while (i<num_switches):
	name = san.Switches[i].switchName
	ip = san.Switches[i].mgmtIP
	user_name = san.Switches[i].userName
	passwd = san.Switches[i].userPassword
	num_flows = len(san.Switches[i].flows)
	j=0
	while (j<num_flows):
		flownames.append(san.Switches[i].flows[j].flowName)
		j += 1
	san_switch.append(BrocadeSANSwitch(name, ip, user_name, passwd, flownames, cmd_string))
	print(san_switch[i].mgmt_ip)

        num_flow_names = len(san_switch[i].flows)
        j=0
        while (j<num_flow_names):
            print(san_switch[i].flows[j].flow_name)
            j += 1
#	san_switch[i].ssh_to_switch()
#	san_switch[i].execute_cmd()
	i += 1

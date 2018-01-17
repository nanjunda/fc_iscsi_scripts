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
    command = []


    def __init__(self, switch_name, mgmt_ip, user_name, user_password, flow_names):
        self.switch_name = switch_name
        self.mgmt_ip = mgmt_ip
        self.user_name = user_name
        self.user_password = user_password
        self.ssh_client_handle =  paramiko.SSHClient()
        self.flow_names = flow_names
        self._create_flow_objects()


    def ssh_to_switch(self):
        self.ssh_client_handle.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client_handle.connect(self.mgmt_ip, username=self.user_name, password=self.user_password)


    def execute_cmd(self,cmd):
        stdin, stdout, stderr = self.ssh_client_handle.exec_command(cmd)
        print(stdout.read().strip())

    def _create_flow_objects(self):
        num_flow_names = len(self.flow_names)
        j=0
        while (j<num_flow_names):
            fl = BrocadeSANFlow(self, self.flow_names[j])
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


    """
    constructor for BrocadeSANFLow class
    """
    def __init__(self, san_switch, flow_name):
        self.flow_name = flow_name
        self.san_switch = san_switch

    """
    method to list all the flows
    """
    def list_flows(self):
        self.san_switch.execute_cmd("flow --show")

    """
    method to clean up command buffer
    """
    def delete_flow_commands(self):
        self.cmd.clear()

    """
    method to show individul flows
    """
    def show_flow(self):
        self.san_switch.execute_cmd("flow --show " + self.flow_name)

    """
    method to show individul flows
    """
    def create_flow(self):
        self.san_switch.execute_cmd("flow --create -feature monitor " + self.flow_name)

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
        san_switch.append(BrocadeSANSwitch(name, ip, user_name, passwd, flownames))
        print(san_switch[i].mgmt_ip)
        san_switch[i].ssh_to_switch()

        num_flow_names = len(san_switch[i].flows)
        j=0
        while (j<num_flow_names):
            print(san_switch[i].flows[j].flow_name)
            san_switch[i].flows[j].show_flow()
            j += 1
        i += 1

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
import re
from io import StringIO
from pprint import pprint
from collections import namedtuple


########################################################################
# Support functions                                                    #
########################################################################

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())

def load_data(file_name):
  with open(file_name, 'r') as file_data:
    return file_data.read().replace('\n', '')
        
def json2obj(file_name): return json.loads(load_data(file_name), object_hook=_json_object_hook)

############################################################
# Brocade Switch Class definition                          #
############################################################

class BrocadeSANSwitch:

    """
    Class:
    Brocade SAN Switch 
    Attributes:
    mgmt_ip: management IP address
    user_name: user name to login
    user_password: user password to login
    """

    ports = []
    flows = []
    command = []
    redirect_output = StringIO()


    def __init__(self, switch_name, mgmt_ip, user_name, user_password):
        self.switch_name = switch_name
        self.mgmt_ip = mgmt_ip
        self.user_name = user_name
        self.user_password = user_password
        self.ssh_client_handle =  paramiko.SSHClient()

    def set_switch_ports(self, ports):
        self._create_port_objects(ports)

    def set_switch_flows(self, flow_names):
        self._create_flow_objects(flow_names)

    def ssh_to_switch(self):
        self.ssh_client_handle.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client_handle.connect(self.mgmt_ip, username=self.user_name, password=self.user_password)

    def execute_cmd(self,cmd):
        stdin, stdout, stderr = self.ssh_client_handle.exec_command(cmd)
        old_stdout = sys.stdout
        sys.stdout=self.redirect_output
        print(stdout.read().strip())
        sys.stdout = old_stdout

    """
    support functions; only internal
    """

    def _create_port_objects(self, _ports):
        num_ports = len(_ports)
        j = 0
        while (j < num_ports):
            _pn = BrocadeSANPort(self, _ports[j][0], _ports[j][1])
            self.ports.append(_pn)
            j += 1 

    def _create_flow_objects(self, _flow_names):
        num_flow_names = len(_flow_names)
        j=0
        while (j<num_flow_names):
            _fl = BrocadeSANFlow(self, _flow_names[j])
            self.flows.append(_fl)
            j += 1

############################################################
# this python script defines Brocade SAN Port as a class   #
# with attributes and methods related to port              #
# such as port name, port id, etc. to start with           #
# and port enable and disable, etc.                        #
############################################################

class BrocadeSANPort:

    port_id = "None"
    port_speed = "None"
    port_state = "None"
    port_type = "None"
    port_wwn = "None"

    """
    constructor for BrocadeSANPort class
    """
    def __init__(self, san_switch, port_number, port_speed):
        self.port_number = port_number
        self.port_speed = port_speed
        self.san_switch = san_switch
        self.get_port_info()

    """
    Set remaining attributes of the port - port speed
    """
    def set_port_attributes(self, port_speed):
        self.port_speed = port_speed

    def get_port_info(self):
        text = self._get_port_info()
        print(text)

    """
    support functions; only internal
    """

    def _get_port_info(self):
        self.san_switch.ssh_to_switch()
        self.san_switch.execute_cmd("switchshow")
        out = self.san_switch.redirect_output.getvalue()

        lines = out.split('\\n')
        matches = []
        pattern = str(self.port_number)
        reg_str = " +" + pattern + " +" + pattern
        print(reg_str)
        reg = re.compile(reg_str)
        for line in lines:
            matches = re.search(reg, line)
            if (matches):
                return line



############################################################
# this python script defines Brocade SAN Flow as an object #
# with flow attributes and methods related to flow         #
############################################################

class BrocadeSANFlow:

    """
    Class:
    Brocade SAN Flow 
    Attributes:
    """


    """
    constructor for BrocadeSANFlow class
    """
    def __init__(self, san_switch, flow_name):
        self.flow_name = flow_name
        self.san_switch = san_switch

    """
    Set remaining attributes of the flow - port, feature, initial step
    """
    def set_flow_attributes(self, port, feature, framesize, cmd):
        self.port = port
        self.feature = feature
        self.framesize = framesize
        self.cmd = cmd

    """
    Execute command that is passed through "self.cmd"
    Uses Python didctionary. map "cmd" to function name
    and index "cmd" to get what function to call
    """
    def exec_cmd(self):
        cmd_issued = { 
                "create" : self.create_flow,
                "show" : self.show_flow,
                "list" : self.list_flows
                }
        cmd_issued[self.cmd]


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

#
# Main script
#
configFile = sys.argv[1]
san_switch = []
flownames = []
framesize = []
port = []
port_numbers = []
port_speed = []
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
                #add port number and port speed as tuple
                port.append((san.Switches[i].flows[j].portNumber, san.Switches[i].flows[j].portSpeed))
                framesize.append(san.Switches[i].flows[j].frameSize)
                j += 1

        san_switch.append(BrocadeSANSwitch(name, ip, user_name, passwd))

        san_switch[i].set_switch_flows(flownames)
        san_switch[i].set_switch_ports(port)

        j=0
        while (j<num_flows):
                san_switch[i].flows[j].set_flow_attributes(san.Switches[i].flows[j].portNumber, san.Switches[i].flows[j].feature, san.Switches[i].flows[j].frameSize, san.Switches[i].flows[j].command)
                j += 1

        print(san_switch[i].mgmt_ip)
        san_switch[i].ssh_to_switch()

        j=0
        while (j<num_flows):
            print(san_switch[i].flows[j].flow_name)
            san_switch[i].flows[j].exec_cmd()
            j += 1

        i += 1

import sys
import paramiko
import re
from io import StringIO
from pprint import pprint
from collections import namedtuple


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
        # This variable will store everything that is sent to the standard output
            stdin, stdout, stderr = self.ssh_client_handle.exec_command(cmd)
            old_stdout = sys.stdout
            sys.stdout=self.redirect_output
            print(stdout.read().strip())
            sys.stdout = old_stdout

    """
    support functions; only internal
    """

    def _create_port_objects(self, _ports):
        num_port_numbers = len(_ports)
        j = 0
        while (j < num_port_numbers):
            _pn = BrocadeSANPort(self, _ports[j])
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
    def __init__(self, san_switch, port_number):
        self.port_number = port_number
        self.san_switch = san_switch
#        self._get_port_info()

    """
    support functions; only internal
    """

    """
    def _get_port_info(self)
        with open("portInfo", "r") as temp_port_info:
            matches = []
            reg = re.compile(r ' +30 +30')
            for line in temp_port_info:
                matches += reg.findall(line)
        temp_port_info.close()
   """


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
    def set_flow_attributes(self, port, feature, cmd):
        self.port = port
        self.feature = feature
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

def _get_port_info(str):
    lines = str.split('\\n')
    matches = []
    reg = re.compile(r' +30 +30')
    for line in lines:
        matches = re.search(r' +30 +30', line)
        if (matches):
            return line

b_switch = BrocadeSANSwitch("server_switch", "10.26.3.194", "admin", "password")
b_switch.ssh_to_switch()
b_switch.execute_cmd("switchshow")

# Then, get the stdout like a string and process it!
out = b_switch.redirect_output.getvalue()
#print(out)

"""
"""
text = _get_port_info(out)
print(text)
words = text.split()
# for each word in the line:
for word in words:
# print the word
    print(word)

#
# this python script will issue portEnable or portDisable command to Brocade SAN switch
# to enable or disable the switch port
# argv 1 - management IP address of the switch
# argv 2 - user name (admin)
# argv 3 - password (password)
# argv 4 - command list file
#
import paramiko
import sys

class BrocadeSANSwitch:

    """
    Class:
    Brocade SAN Switch 
    Attributes:
    mgmtIp: management IP address
    userName: user name to login
    UserPassword: user password to login
    """


    def __init__(self, mgmtIP, userName, userPassword):
        self.mgmtIP = mgmtIP
        self.userName = userName
        self.userPassword = userPassword
        self.ssh_client_handle = paramiko.SSHClient()

    def ssh_to_switch(self):
        self.ssh_client_handle.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client_handle.connect(self.mgmtIP, username=self.userName, password=self.userPassword, port=22)

    def set_cmd_string(self, cmd):
        self.command = cmd

    def execute_cmd(self):
        stdin, stdout, stderr = self.ssh_client_handle.exec_command(self.command)
        print(stdout.read().strip())

ip = sys.argv[1]
userName = sys.argv[2]
passWord = sys.argv[3]
argc = len(sys.argv)

#Next arg count (variable number of command strings)
i=4

cmd_list = []

while (i < argc):
    cmd_list.append(sys.argv[i])
    i += 1

sanSwitch = BrocadeSANSwitch(ip, userName, passWord)
sanSwitch.ssh_to_switch()

j = 0
i = len(cmd_list)
while (j < i):
    print (cmd_list[j])
    sanSwitch.set_cmd_string(cmd_list[j])
    sanSwitch.execute_cmd()
    j += 1

#
# this python script will issue portEnable or portDisable command to Brocade SAN switch
# to enable or disable the switch port
# argv 1 - management IP address of the switch
# argv 2 - user name (admin)
# argv 3 - password (password)
# argv 4 - flow name
# argv 5 - frame size
#
import paramiko
import time
import sys

def ssh_connector(ip, userName, passWord):
 ssh = paramiko.SSHClient()
 ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 ssh.connect(ip, username=userName, password=passWord, port=22)
 return (ssh)


def execute_cmd(ssh, command):
 stdin, stdout, stderr = ssh.exec_command(command)
 print(stdout.read().strip())



ip = sys.argv[1]
userName = sys.argv[2]
passWord = sys.argv[3]
flowName = sys.argv[4]
frameSize = sys.argv[5]

ssh = ssh_connector(ip, userName, passWord)
cmd_string = "flow --deactivate " + flowName
execute_cmd(ssh, cmd_string)
time.sleep(9)
cmd_string = "flow --control " + flowName + " -feature monitor,generator -size " + frameSize
execute_cmd(ssh, cmd_string)
time.sleep(5)
cmd_string = "flow --activate " + flowName
execute_cmd(ssh, cmd_string)

#
# this python script will issue portEnable or portDisable command to Brocade SAN switch
# to enable or disable the switch port
# argv 1 - management IP address of the switch
# argv 2 - user name (admin)
# argv 3 - password (password)
# argv 4 - Port number
# argv 5 - "portEnable" or "portDisable"
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
 channel = ssh.invoke_shell()
 channel.send(command)
 while not channel.recv_ready():
  time.sleep(3)
 out = channel.recv(9999)
 print(out.decode("ascii"))



ip = sys.argv[1]
userName = sys.argv[2]
passWord = sys.argv[3]
portNum = sys.argv[4]
cmd = sys.argv[5]

ssh = ssh_connector(ip, userName, passWord)
cmd_string = cmd + " " + portNum + "\n"
execute_cmd(ssh, cmd_string)

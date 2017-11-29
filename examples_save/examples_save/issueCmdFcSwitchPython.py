# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
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
 channel.send('exit\n')
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

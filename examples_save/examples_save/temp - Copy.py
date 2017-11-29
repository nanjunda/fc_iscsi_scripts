# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import paramiko
import time

def ssh_connector(ip, userName, passWord, command):
 ssh = paramiko.SSHClient()
 ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 ssh.connect(ip, username=userName, password=passWord, port=22)
 channel = ssh.invoke_shell()
 channel.send('cfgshow\n')
 channel.send('exit\n')
 while not channel.recv_ready():
  time.sleep(3)
 out = channel.recv(9999)
 print(out.decode("ascii"))

ip = "10.26.9.82"
userName = "admin"
passWord = "password"
ssh_connector(ip, userName, passWord, 'show running-config\n')

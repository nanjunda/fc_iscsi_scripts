import pexpect
import sys
import pandas as pd
import sys
import os
import collections
import xlsxwriter
import json

postfix=' | exc more'
passwd_expect_string='assword: '
"""
JSON CODE

json_param_file = sys.argv[1]

with open(json_param_file, "r") as f:
	buf = f.read()
data = json.loads(buf)

read_pct = list(data["read_pct"])
size_vals = list(data["io_size"])
qdepth_vals = list(data["que_depth"])
congestion_pct = data["congestion"]
disrupt_type = data["disruption"]
switch_ip = data["switch_ip"]
user_name = data["user_name"]
user_passwd = data["user_passwd"]
switch_prompt = data["switch_prompt"]
print(read_pct, size_vals, qdepth_vals, congestion_pct, disrupt_type, switch_ip, user_name, user_passwd, switch_prompt)

for port_info in data["ports"]:
    p_info = port_info["port_num"] 
    p_type = port_info["port_type"] 
    print(p_info, p_type)


JSON CODE
"""


json_param_file = sys.argv[1]

with open(json_param_file, "r") as f:
	buf = f.read()
data = json.loads(buf)

read_pct = list(data["read_pct"])
size_vals = list(data["io_size"])
qdepth_vals = list(data["que_depth"])
congestion_pct = data["congestion"]
disrupt_type = data["disruption"]
switch_ip = data["switch_ip"]
user = data["user_name"]
pwd = data["user_passwd"]
switch_prompt = data["switch_prompt"]
ports = []

print(switch_ip)
print(user)
print(pwd)
print(switch_prompt)

ports = [
            { 'port_num' : '12/0/49', 'port_type' : 'fo' }, 
            { 'port_num' : '12/0/50', 'port_type' : 'fo' } 
        ]

child = pexpect.spawn('ssh -l %s %s'%(user, switch_ip))
child.expect(passwd_expect_string)
send_str = pwd
child.sendline(send_str)
child.expect(switch_prompt)

for port_info in data["ports"]:
    p_num = port_info["port_num"] 
    p_type = port_info["port_type"] 
    send_str = 'show int ' + p_type + ' ' + p_num + postfix
    child.sendline(send_str)
    child.expect(switch_prompt)
    buf = str(child.before, 'utf-8')
    print(buf)

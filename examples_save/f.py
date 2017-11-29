import sys
import pexpect

user='admin'
host='10.26.3.161'
pwd='password'

child = pexpect.spawn('ssh -l %s %s'%(user, host))
child.expect('*assword:*')
child.send(pwd+'\r')
child.expect('*#: ')

"""
#!/bin/bash

PWD="password"

/usr/bin/expect << EOD
spawn ssh admin@10.26.3.161
expect *assword:*
send -- "$PWD\r" 
expect "*# "
send -- "\r"
expect "*# "
send -- "sh int status\r"
expect "*More*"
send -- " "
expect "*More*"
send -- " "
expect "*# "
puts " The output is \$expect_out(buffer) "
EOD
echo "you're out"
"""

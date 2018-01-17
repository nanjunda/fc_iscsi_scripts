import pexpect
import sys

host=sys.argv[1]
user=sys.argv[2]
pwd=sys.argv[3]

child = pexpect.spawn('ssh -l %s %s'%(user, host))
child.expect('assword: ')
child.send(pwd+'\r')
child.expect("etwork Operating System Software\r\nadmin connected from 10.197.192.245 using ssh on sw12\r\n\x1b\[\?7hsw12# ")
child.send('fastboot\r')
child.expect_exact('fastboot\r\nAre you sure you want to fastboot the switch? [y/n]:')
child.send('y\r')

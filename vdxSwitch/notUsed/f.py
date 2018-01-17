import pexpect

user='admin'
host='10.26.3.161'
pwd='password'

child = pexpect.spawn('ssh -l %s %s'%(user, host))
child.expect('assword: ')
child.send(pwd+'\r')
child.expect("etwork Operating System Software\r\nadmin connected from 10.197.192.245 using ssh on sw12\r\n\x1b\[\?7hsw12# ")
child.send('fastboot\r')
child.expect_exact('fastboot\r\nAre you sure you want to fastboot the switch? [y/n]:')
child.send('y\r')

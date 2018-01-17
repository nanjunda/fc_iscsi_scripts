import pexpect
import sys
from pprint import pprint

host=sys.argv[1]
user=sys.argv[2]
pwd=sys.argv[3]
port_type="fo"
port_num="12/0/49"
postfix=' | exc more'

child = pexpect.spawn('ssh -l %s %s'%(user, host))
child.expect('assword: ')
send_str = pwd
child.sendline(send_str)
child.expect('sw13# ')
send_str = 'show int ' + port_type + ' ' + port_num + postfix
child.sendline(send_str)
child.expect('sw13# ')
buf = str(child.before, 'utf-8')
print(buf)

#!/usr/bin/env python

from __future__ import print_function

from __future__ import absolute_import

import pexpect
import sys, getpass



USAGE = '''passmass host1 host2 host3 . . .'''
#COMMAND_PROMPT=r'\*admin\> '
COMMAND_PROMPT=r'\r\nFabricA-Server:FID128:admin\> '
TERMINAL_PROMPT=r'Terminal type\?'
TERMINAL_TYPE='vt100'
SSH_NEWKEY=r'Are you sure you want to continue connecting \(yes/no\)\?'
FASTBOOT='\r\nAre you sure you want to reboot the switch [y/n]?'

def login(host, user, password):

    child = pexpect.spawn('ssh -l %s %s'%(user, host))
    fout = file ("LOG.TXT","wb")
    child.logfile_read = fout #use child.logfile to also log writes (passwords!)

    i = child.expect([pexpect.TIMEOUT, SSH_NEWKEY, '[Pp]assword: '])
    if i == 0: # Timeout
        print('ERROR!')
        print('SSH could not login. Here is what SSH said:')
        print(child.before, child.after)
        sys.exit (1)
    if i == 1: # SSH does not have the public key. Just accept it.
        child.sendline ('yes')
        child.expect ('[Pp]assword: ')
    child.sendline(password)
    # Now we are either at the command prompt or
    # the login process is asking for our terminal type.
    i = child.expect(COMMAND_PROMPT)
    return child

# fastboot switch
def fastboot_switch(child, user, password):

    child.sendline('fastboot')
    i = child.expect_exact(FASTBOOT)
    child.sendline('y')

def main():

    if len(sys.argv) <= 1:
        print(USAGE)
        return 1

    host = sys.argv[1]
    user = sys.argv[2]
    password = sys.argv[3]

    child = login(host, user, password)
    if child == None:
        print('Could not login to host:', host)
        exit(1)
    print('Rebooting switch:', host)
    fastboot_switch(child, user, password)
    child.expect(COMMAND_PROMPT)
    child.sendline('exit')

if __name__ == '__main__':
    main()

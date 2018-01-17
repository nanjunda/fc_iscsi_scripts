#
# this python script will issue portEnable or portDisable command to Brocade VDX switch
# to enable or disable the switch port
# argv 1 - management IP address of the switch
# argv 2 - user name (admin)
# argv 3 - password (password)
# argv 4 - Port number
# argv 5 - port type (tengigabitethernet, etc)
# argv 6 - "portEnable" or "portDisable"
#
import pynos.device
import time
import sys
import datetime
import os

from os import path


def connect_to_switch(ip, userName, passWord):
    conn= (ip, 22)
    auth= (userName, passWord)
    dev = pynos.device.Device(conn=conn, auth=auth)
    return (dev)



"""
ip = sys.argv[1]
user_name = sys.argv[2]
password = sys.argv[3]
port_num = sys.argv[4]
port_type=sys.argv[5]
cmd = sys.argv[6]
"""
var1=180
var2=180
isl_var=60
waitvar=2
t10=10
counter = 0

maim_start_file='/tmp/.maim_test_start'
maim_test_running='/tmp/.maim_test_running'


ip = '10.26.3.161'
user_name = 'admin'
password = 'password'
port_num_49 = '12/0/49'
port_num_50 = '12/0/50'
port_type='fortygigabitethernet'

conn_handle = connect_to_switch(ip, user_name, password)
while True:
    if path.exists(maim_start_file):
        os.remove(maim_start_file)
        ts='{:%y%m%d%H%M%S}'.format(datetime.datetime.now())
        print(ts + ': Going to initial sleep for %d secs' % var2)
        sys.stdout.flush()
        time.sleep(var2)
        while True:
            if path.exists(maim_test_running):
                counter += 1
                ts='{:%y%m%d%H%M%S}'.format(datetime.datetime.now())
                print(ts + ': Port Disabled')
                sys.stdout.flush()
                conn_handle.interface.admin_state(int_type=port_type, name=port_num_49, enabled=False)
                conn_handle.interface.admin_state(int_type=port_type, name=port_num_50, enabled=False)
                time.sleep(isl_var)
                ts='{:%y%m%d%H%M%S}'.format(datetime.datetime.now())
                print(ts + ': Port Enabled')
                sys.stdout.flush()
                conn_handle.interface.admin_state(int_type=port_type, name=port_num_49, enabled=True)
                conn_handle.interface.admin_state(int_type=port_type, name=port_num_50, enabled=True)
                t=10
                while (t <= var1):
                    if path.exists(maim_test_running):
                        ts='{:%y%m%d%H%M%S}'.format(datetime.datetime.now())
                        print(ts + ': sleeping % secs after ISL enable' % t)
                        sys.stdout.flush()
                        time.sleep(t10)
                        t += 10 
                    else:
                        ts='{:%y%m%d%H%M%S}'.format(datetime.datetime.now())
                        print(ts + ': End maim test run breaking - time = ' + str(t))
                        sys.stdout.flush()
                        t = 0
                        break
                if (t == 0 or t > var1):
                    try:
                        os.remove(maim_test_running)
                    except OSError:
                        pass
                    break
    else:
        ts='{:%y%m%d%H%M%S}'.format(datetime.datetime.now())
        print(ts + ': Waiting for command to start')
        time.sleep(waitvar)
        sys.stdout.flush()

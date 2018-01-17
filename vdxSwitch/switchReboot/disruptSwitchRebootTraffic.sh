#
# Use the python script - sanSwitchPortManipulate.py to enable or disable switch port
# this script will timestamp when the command was issued and when the command exits
# var1 - between disabling and enabling of the port, wait for var1 secs (short time)
# var2 - once port is disabled and enabled, sleep for var2 secs (longer time)
# var1 and var2 are random numbers between the range of 9 to 19 and 30 to 400
# this loop goes on for ever until is is cancelled using "CONTROL-C"
#

PYSCRIPT="/home/Administrator/scripts"
DISRUPT_PYSCRIPT="$PYSCRIPT/vdxSwitch/switchReboot"

echo "Make sure that Spirent is running"
read b
echo "Confirm"
read a
# sleep for 3 minutes (180 secs) first, switch reboot and then sleep for 5 minutes (300 secs)
var1=550
var2=300
waitvar=2
switch_ip_addr='10.26.3.161'
user='admin'
passwd='password'

rm -rf /tmp/.maim_test_start /tmp/.maim_test_running
while (true)
do
	if [ -e /tmp/.maim_test_start ]
	then
		rm -rf /tmp/.maim_test_start
		counter=0
		DATE_TIME=`date +%y%m%d%H%M%S`
		echo "${DATE_TIME} : Start maim test run sleeping initial $var2 secs"
		sleep $var2
		DATE_TIME=`date +%y%m%d%H%M%S`
		echo "${DATE_TIME} : Start VDX switch reboot "
		while (true)
		do
			if [ -e /tmp/.maim_test_running ]
			then
				((counter=counter+1))
				echo -n "Counter = $counter  "
				DATE_TIME=`date +%y%m%d%H%M%S`
				echo "${DATE_TIME} : About reboot switch"
				bash $DISRUPT_PYSCRIPT/vdxRemoteReboot.sh $switch_ip_addr $user $passwd
###############################################################################################################
#				python ${PYSCRIPT}/disruptVDX_SwitchTraffic.py $switch_ip_addr $user $passwd  #
###############################################################################################################
				echo -n "Counter = $counter  "
				DATE_TIME=`date +%y%m%d%H%M%S`
				echo "${DATE_TIME} : Switch rebooted"
			fi

			if [ -e /tmp/.maim_test_running ]
			then
				DATE_TIME=`date +%y%m%d%H%M%S`
				echo "${DATE_TIME} : sleeping $var1 secs after switch reboot"
				sleep $var1
				if ((counter == 1))
				then
					rm -rf /tmp/.maim_test_running
				fi
			else
				DATE_TIME=`date +%y%m%d%H%M%S`
				echo "${DATE_TIME} : End maim test run breaking - counter = $counter"
				break
			fi
		done
	else
		DATE_TIME=`date +%y%m%d%H%M%S`
		echo "${DATE_TIME} : Waiting for command to start"
		sleep $waitvar
	fi
done

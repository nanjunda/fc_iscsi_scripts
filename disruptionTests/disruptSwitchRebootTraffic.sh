#
# Use the python script - disruptFC_SwitchTraffic.py to reboot FC switch 
# this script will timestamp when the command was issued and when the command exits
# var1 - wait after switch reboot for var1 secs (longer time)
# var2 - sleep for var2 secs before switch reboot(shorter time)
# this loop goes on for ever until is is cancelled using "CONTROL-C"
#

PYSCRIPT="C:\Users\nsomayaj\Box_Sync\BroadcomTransition\SolutionIdeas\FC_iSCSI_Comparison\scripts\pyScript"
DISRUPT_PYSCRIPT="${PYSCRIPT}/disruptionTests"

# sleep for 3 minutes (180 secs) first, switch reboot and then sleep for 5 minutes (300 secs)
var1=300
var2=180
waitvar=2
switch_ip_addr='10.26.3.194'
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
		echo "${DATE_TIME} : Start FC switch reboot "
		while (true)
		do
			if [ -e /tmp/.maim_test_running ]
			then
				((counter=counter+1))
				echo -n "Counter = $counter  "
				DATE_TIME=`date +%y%m%d%H%M%S`
				echo "${DATE_TIME} : About reboot switch"
				python ${DISRUPT_PYSCRIPT}/disruptFC_SwitchTraffic.py $switch_ip_addr $user $passwd
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

#
# Use the python script - sanSwitchPortManipulate.py to enable or disable switch port
# this script will timestamp when the command was issued and when the command exits
# var1 - between disabling and enabling of the port, wait for var1 secs (short time)
# var2 - once port is disabled and enabled, sleep for var2 secs (longer time)
# var1 and var2 are random numbers between the range of 9 to 19 and 30 to 400
# this loop goes on for ever until is is cancelled using "CONTROL-C"
#

#PYSCRIPT="C:\Users\nsomayaj\Box_Sync\BroadcomTransition\SolutionIdeas\FC_iSCSI_Comparison\scripts\pyScript"
PYSCRIPT="/home/Administrator/scripts"
SANSWITCH_PYSCRIPT="${PYSCRIPT}/sanSwitch"

# sleep for 3 minutes (180 secs) first, disrupt for 1 minute (60 secs) and then sleep for 3 minutes (180 secs)
# we wil have 60 secs ISL down
var1=180
var2=180
isl_var=60
waitvar=2

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
		echo "${DATE_TIME} : Start ISL manipulation "
		while (true)
		do
			if [ -e /tmp/.maim_test_running ]
			then
				((counter=counter+1))
				echo -n "Counter = $counter  "
				DATE_TIME=`date +%y%m%d%H%M%S`
				echo "${DATE_TIME} : ISL  Disabled"
				python3 ${SANSWITCH_PYSCRIPT}/sanSwitchAnyCommand.py 10.26.3.194 admin password "portdisable 40"  "portdisable 43" "sleep $isl_var" "portenable 40"  "portenable 43"
				echo -n "Counter = $counter  "
				DATE_TIME=`date +%y%m%d%H%M%S`
				echo "${DATE_TIME} : ISL Enabled"
			fi

			if [ -e /tmp/.maim_test_running ]
			then
				DATE_TIME=`date +%y%m%d%H%M%S`
				echo "${DATE_TIME} : sleeping $var1 secs after ISL enable"
				sleep $var1
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

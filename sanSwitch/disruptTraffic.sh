#
# Use the python script - sanSwitchPortManipulate.py to enable or disable switch port
# this script will timestamp when the command was issued and when the command exits
# var1 - between disabling and enabling of the port, wait for var1 secs (short time)
# var2 - once port is disabled and enabled, sleep for var2 secs (longer time)
# var1 and var2 are random numbers between the range of 9 to 19 and 30 to 400
# this loop goes on for ever until is is cancelled using "CONTROL-C"
#

#PYSCRIPT="C:\Users\nsomayaj\Box_Sync\BroadcomTransition\SolutionIdeas\FC_iSCSI_Comparison\scripts\pyScript"
PYSCRIPT="."

#sleep for 2 minutes first and then sleep for 3 minutes in the loop with 30 secs ISL down
var1=180
var2=120
isl_var=30
counter=0

sleep $var2
DATE_TIME=`date +%y%m%d%H%M%S`
echo "${DATE_TIME} : Start ISL manipulation "
while (true)
do
	((counter=counter+1))
	echo -n "Counter = $counter  "
	DATE_TIME=`date +%y%m%d%H%M%S`
	echo "${DATE_TIME} : ISL  Disabled"
	python ${PYSCRIPT}/sanSwitchAnyCommand.py 10.26.3.194 admin password "portdisable 40"  "portdisable 43" "sleep $isl_var" "portenable 40"  "portenable 43"
	echo -n "Counter = $counter  "
	DATE_TIME=`date +%y%m%d%H%M%S`
	echo "${DATE_TIME} : ISL Enabled"
	sleep $var1
done
DATE_TIME=`date +%y%m%d%H%M%S`
echo "${DATE_TIME} : End ISL manipulation "

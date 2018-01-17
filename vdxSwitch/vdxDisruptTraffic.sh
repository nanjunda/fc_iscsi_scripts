#
# Use the python script - vdxSwitchPortManipulate.py to enable or disable switch port
# this script will timestamp when the command was issued and when the command exits
# var1 - between disabling and enabling of the port, wait for var1 secs (short time)
# var2 - once port is disabled and enabled, sleep for var2 secs (longer time)
# var1 and var2 are random numbers between the range of 9 to 19 and 30 to 400
# this loop goes on for ever until is is cancelled using "CONTROL-C"
#

PYSCRIPT="C:\Users\nsomayaj\Box_Sync\BroadcomTransition\SolutionIdeas\FC_iSCSI_Comparison\scripts\vdxSwitch"

#sleep for 4 minutes
var1=240
var2=240
while (true)
do
	DATE_TIME=`date +%y%m%d%H%M%S`
	echo "${DATE_TIME} : Port 12/0/50 Disabled"
	python ${PYSCRIPT}/vdxSwitchPortManipulate.py 10.26.3.161 admin password 12/0/50 FortyGigabitEthernet 
	sleep $var1
	DATE_TIME=`date +%y%m%d%H%M%S`
	echo "${DATE_TIME} : Port 12/0/50 Enabled"
	python ${PYSCRIPT}/vdxSwitchPortManipulate.py 10.26.3.161 admin password 12/0/50 FortyGigabitEthernet
	sleep $var2
done

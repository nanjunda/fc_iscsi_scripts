#
# this script is to drive the congestion testing for FC switches to benchmark against iSCSI
# (see run_iscsi_congestion_tests.sh in this directory). it will configure the SIMPORTS to
# generate traffic to cause congestion
# uses Windows utility "logman" to capture CPU info such as idle time, process time, etc.
#

# directory where the scritps are
PYSCRIPT="/cygdrive/C/Users/nsomayaj/Box_Sync/BroadcomTransition/SolutionIdeas/FC_iSCSI_Comparison/scripts"
SANSWITCH_PYSCRIPT="${SANSWITCH_SCRIPT}/sanSwitch"


#
# args  - mgmt ip, flow name, frame size, port #, port speed
#
change_switch_config()
{
python ${SANSWITCH_PYSCRIPT}/sanSwitchAnyCommand.py $1 admin password "flow --deactivate $2" "flow --control $2 -feature monitor,generator -size $3" "flow --activate $2" "portcfgspeed $4 $5"
}

# configure the sim ports with speed and framesize
# uses the ports 30 and 31 in both two switches
change_switch_config "10.26.3.194" "flowcase4" "2048" "31" "8"
change_switch_config "10.26.2.207" "flowcase3" "2048" "31" "8"


#
# 60
#
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Start the perfmon"
logman start FC-iSCSI
sleep 60
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Starting 60% load"
#
change_switch_config "10.26.3.194" "flowcase2" "164" "30" "4"
change_switch_config "10.26.2.207" "flowcase1" "164" "30" "4"
#
echo -n "Check Spirent for 60% load"; read a;echo -n "Confirm:"; read a
cd Run8_FC_Congestion_60
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Starting test run"
sh F100_FC_R70_W30_Q64_B8K >60Out 2>&1
cd ..
sleep 120
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Stop the perfmon"
logman stop FC-iSCSI
#
#
# 70
#
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Start the perfmon"
logman start FC-iSCSI
sleep 60
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Starting 70% load"
#
change_switch_config "10.26.3.194" "flowcase2" "140" "30" "8"
change_switch_config "10.26.2.207" "flowcase1" "140" "30" "8"
#
echo -n "Check Spirent 70"; read a
echo -n "Confirm:"; read a
cd Run8_FC_Congestion_70
sh F100_FC_R70_W30_Q64_B8K >70Out 2>&1
DATE_TIME=`date +%y%m%d%H%m%S`: echo -n "${DATE_TIME}:  "; echo "Starting test run"
cd ..
sleep 120
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Stop the perfmon"
logman stop FC-iSCSI
#
#
# 80
#
echo "Start the perfmon" 
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; 
logman start FC-iSCSI
sleep 60
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Starting 80% load"
#
change_switch_config "10.26.3.194" "flowcase2" "224" "30" "8"
change_switch_config "10.26.2.207" "flowcase1" "224" "30" "8"
#
echo -n "Check Spirent 80"; read a
echo -n "Confirm:"; read a
cd Run8_FC_Congestion_80
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  ": echo "Starting test run"
sh F100_FC_R70_W30_Q64_B8K >80Out 2>&1
cd ..
sleep 120
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Stop the perfmon"
logman stop FC-iSCSI

#
# 90
#
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Start the perfmon"
logman start FC-iSCSI
sleep 60
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Starting 90% load"
#
change_switch_config "10.26.3.194" "flowcase2" "296" "30" "16"
change_switch_config "10.26.2.207" "flowcase1" "296" "30" "16"
#
echo -n "Check Spirent 90"; read a
echo -n "Confirm:"; read a
cd Run8_FC_Congestion_90
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Starting test run"
sh F100_FC_R70_W30_Q64_B8K >90Out 2>&1
cd ..
sleep 120
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Stop the perfmon"
logman stop FC-iSCSI

#
# 95
#
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Start the perfmon"
logman start FC-iSCSI
sleep 60
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Starting 95% load"
#
change_switch_config "10.26.3.194" "flowcase2" "328" "30" "16"
change_switch_config "10.26.2.207" "flowcase1" "328" "30" "16"
#
echo -n "Check Spirent 95"; read a
echo -n "Confirm:"; read a
cd Run8_FC_Congestion_95
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Starting test run"
sh F100_FC_R70_W30_Q64_B8K >95Out 2>&1
cd ..
sleep 120
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Stop the perfmon"
logman stop FC-iSCSI

#
# 100
#
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Start the perfmon"
logman start FC-iSCSI
sleep 60
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Starting 100% load"
#
change_switch_config "10.26.3.194" "flowcase2" "364" "30" "16"
change_switch_config "10.26.2.207" "flowcase1" "364" "30" "16"
#
echo -n "Check Spirent 100"; read a
echo -n "Confirm:"; read a
cd Run8_FC_Congestion_100
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Starting test run"
sh F100_FC_R70_W30_Q64_B8K >100Out 2>&1
cd ..
sleep 120
DATE_TIME=`date +%y%m%d%H%m%S`; echo -n "${DATE_TIME}:  "; echo "Stop the perfmon"
logman stop FC-iSCSI

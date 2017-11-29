#
# this script is to drive the congestion testing for FC switches to benchmark against iSCSI
# (see run_iscsi_congestion_tests.sh in this directory). it will configure the SIMPORTS to
# generate traffic to cause congestion
# uses Windows utility "logman" to capture CPU info such as idle time, process time, etc.
#

# directory where the scritps are
#PYSCRIPT="/cygdrive/C/Users/nsomayaj/Box_Sync/BroadcomTransition/SolutionIdeas/FC_iSCSI_Comparison/scripts"
PYSCRIPT="/home/Administrator/scripts"
SANSWITCH_PYSCRIPT="${PYSCRIPT}/sanSwitch"


#
# args  - mgmt ip, flow name, frame size, port #, port speed
#
change_switch_config()
{
python3 ${SANSWITCH_PYSCRIPT}/sanSwitchAnyCommand.py $1 admin password "flow --deactivate $2" "flow --control $2 -feature monitor,generator -size $3" "flow --activate $2" "portcfgspeed $4 $5"
}

#
# run tests arguments are:
# load percentage (60, 70, 80, 90, 95, 100), frame size,
# port speed, script directory name, script file name
run_tests()
{
	load_pct=$1
	frame_size=$2
	port_speed=$3
	script_dir=$4
	script_file=$5

	server_sw_ip="10.26.3.194"
	server_sw_flow="flowcase2"
	server_sw_port_no="30"
	storage_sw_ip="10.26.2.207"
	storage_sw_flow="flowcase1"
	storage_sw_port_no="30"



	DATE_TIME=`date +%y%m%d%H%M%S`; echo -n "${DATE_TIME}:  "; echo "Starting ${load_pct}% load"
	#
	change_switch_config ${server_sw_ip} ${server_sw_flow} ${2}  ${server_sw_port_no} ${port_speed}
	change_switch_config ${storage_sw_ip} ${storage_sw_flow} ${2}  ${storage_sw_port_no} ${port_speed}
	#
	echo -n "Check Spirent for ${load_pct}% load"; read a;echo -n "Confirm:"; read a
	current_working_dir=`pwd`
	cd "${script_dir}"
	DATE_TIME=`date +%y%m%d%H%M%S`; echo -n "${DATE_TIME}:  "; echo "Starting test run"
	sh "${script_file}" > "${load_pct}Out" 2>&1
	cd ${current_working_dir}
	sleep 120
}



# configure the sim ports with speed and framesize
# uses the ports 30 and 31 in both two switches
change_switch_config "10.26.3.194" "flowcase4" "2048" "31" "8"
change_switch_config "10.26.2.207" "flowcase3" "2048" "31" "8"


# port disruption
#SCRIPT_TO_RUN="F100_FC_D420_R70_W30_logman.sh"
#CD_TO="port_disruption_fc"

#switch reboot
SCRIPT_TO_RUN="F100_FC_D490_R70_W30_logman.sh"
CD_TO="switch_disruption_fc"
#
#run_tests  "60" "164" "4" "60PCT_FC_Congestion/${CD_TO}" ${SCRIPT_TO_RUN}
#run_tests  "70" "140" "8" "70PCT_FC_Congestion/${CD_TO}" ${SCRIPT_TO_RUN}
#run_tests  "80" "224" "8" "80PCT_FC_Congestion/${CD_TO}" ${SCRIPT_TO_RUN}
#run_tests  "90" "296" "16" "90PCT_FC_Congestion/${CD_TO}" ${SCRIPT_TO_RUN}
run_tests  "95" "328" "16" "95PCT_FC_Congestion/${CD_TO}" ${SCRIPT_TO_RUN}
#run_tests  "100" "364" "16" "100PCT_FC_Congestion/${CD_TO}" ${SCRIPT_TO_RUN}

#
# this script is to drive the congestion testing for FC switches to benchmark against iSCSI
# (see run_iscsi_congestion_tests.sh in this directory). it will configure the SIMPORTS to
# generate traffic to cause congestion
# uses Windows utility "logman" to capture CPU info such as idle time, process time, etc.
#

# directory where the scritps are
PYSCRIPT="/cygdrive/C/Users/nsomayaj/Box_Sync/BroadcomTransition/SolutionIdeas/FC_iSCSI_Comparison/scripts"
SANSWITCH_PYSCRIPT="${SANSWITCH_SCRIPT}/sanSwitch"
PERFMON_LOG_DIR="/cygdrive/C/PerfLogs/Admin/FC-iSCSI"


#
# run tests arguments are:
# load percentage (60, 70, 80, 90, 95, 100), frame size,
# port speed, script directory name, script file name
logman_init()
{

	mkdir -p perfmon_logs
	DATE_TIME=`date +%y%m%d%H%M%S`; echo -n "${DATE_TIME}:  "; echo "Cleanup Perfmon Log Directory"
	logman stop FC-iSCSI
	rm -rf  ${PERFMON_LOG_DIR}/WIN*
	sleep 5
}

logman_start()
{

	DATE_TIME=`date +%y%m%d%H%M%S`; echo -n "${DATE_TIME}:  "; echo "Start the perfmon"
	logman start FC-iSCSI
	sleep 5
}


logman_stop()
{

	PWD_DIR=`pwd`
	cd ${PERFMON_LOG_DIR}/WIN*
	cp -rp Run* ${PWD_DIR}/$1
	cd ${PWD_DIR}
	DATE_TIME=`date +%y%m%d%H%M%S`; echo -n "${DATE_TIME}:  "; echo "Stop the perfmon"
	logman stop FC-iSCSI
	mv ${PERFMON_LOG_DIR}/WIN* perfmon_logs
	sleep 5
}

logman_init
logman_start
sleep 10
logman_stop foo.log

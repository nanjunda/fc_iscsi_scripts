PERFMON_LOG_DIR="/cygdrive/C/PerfLogs/Admin/FC-iSCSI"

# run tests arguments are:
# load percentage (60, 70, 80, 90, 95, 100), frame size,
# port speed, script directory name, script file name
logman_init()
{
	DATE_TIME=`date +%y%m%d%H%M%S`; echo -n "${DATE_TIME}:  "; echo "Cleanup Perfmon Log Directory"
	logman stop FC-iSCSI
	rm -rf  ${PERFMON_LOG_DIR}/WIN* /tmp/.maim_test_start /tmp/.maim_test_running perfmon_logs
	mkdir -p perfmon_logs
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
	cp -rp Run* ${PWD_DIR}
	cd ${PWD_DIR}
	DATE_TIME=`date +%y%m%d%H%M%S`; echo -n "${DATE_TIME}:  "; echo "Stop the perfmon"
	logman stop FC-iSCSI
	mv ${PERFMON_LOG_DIR}/WIN* perfmon_logs
	sleep 5
}

logman_init
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b4k -%100:r70,w30,x0,f100 -Q8 -d425 -M600 -ftargets.dat > ${TS}_Q8_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q8_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q8_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q8_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q8_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b8k -%100:r70,w30,x0,f100 -Q8 -d425 -M600 -ftargets.dat > ${TS}_Q8_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q8_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q8_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q8_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q8_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b16k -%100:r70,w30,x0,f100 -Q8 -d425 -M600 -ftargets.dat > ${TS}_Q8_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q8_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q8_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q8_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q8_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b32k -%100:r70,w30,x0,f100 -Q8 -d425 -M600 -ftargets.dat > ${TS}_Q8_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q8_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q8_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q8_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q8_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b64k -%100:r70,w30,x0,f100 -Q8 -d425 -M600 -ftargets.dat > ${TS}_Q8_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q8_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q8_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q8_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q8_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b128k -%100:r70,w30,x0,f100 -Q8 -d425 -M600 -ftargets.dat > ${TS}_Q8_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q8_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q8_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q8_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q8_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b4k -%100:r70,w30,x0,f100 -Q16 -d425 -M600 -ftargets.dat > ${TS}_Q16_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q16_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q16_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q16_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q16_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b8k -%100:r70,w30,x0,f100 -Q16 -d425 -M600 -ftargets.dat > ${TS}_Q16_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q16_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q16_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q16_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q16_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b16k -%100:r70,w30,x0,f100 -Q16 -d425 -M600 -ftargets.dat > ${TS}_Q16_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q16_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q16_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q16_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q16_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b32k -%100:r70,w30,x0,f100 -Q16 -d425 -M600 -ftargets.dat > ${TS}_Q16_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q16_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q16_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q16_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q16_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b64k -%100:r70,w30,x0,f100 -Q16 -d425 -M600 -ftargets.dat > ${TS}_Q16_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q16_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q16_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q16_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q16_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b128k -%100:r70,w30,x0,f100 -Q16 -d425 -M600 -ftargets.dat > ${TS}_Q16_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q16_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q16_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q16_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q16_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b4k -%100:r70,w30,x0,f100 -Q32 -d425 -M600 -ftargets.dat > ${TS}_Q32_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q32_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q32_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q32_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q32_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b8k -%100:r70,w30,x0,f100 -Q32 -d425 -M600 -ftargets.dat > ${TS}_Q32_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q32_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q32_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q32_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q32_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b16k -%100:r70,w30,x0,f100 -Q32 -d425 -M600 -ftargets.dat > ${TS}_Q32_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q32_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q32_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q32_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q32_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b32k -%100:r70,w30,x0,f100 -Q32 -d425 -M600 -ftargets.dat > ${TS}_Q32_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q32_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q32_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q32_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q32_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b64k -%100:r70,w30,x0,f100 -Q32 -d425 -M600 -ftargets.dat > ${TS}_Q32_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q32_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q32_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q32_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q32_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b128k -%100:r70,w30,x0,f100 -Q32 -d425 -M600 -ftargets.dat > ${TS}_Q32_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q32_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q32_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q32_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q32_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b4k -%100:r70,w30,x0,f100 -Q64 -d425 -M600 -ftargets.dat > ${TS}_Q64_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q64_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q64_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q64_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q64_R70_W30_B4k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b8k -%100:r70,w30,x0,f100 -Q64 -d425 -M600 -ftargets.dat > ${TS}_Q64_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q64_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q64_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q64_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q64_R70_W30_B8k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b16k -%100:r70,w30,x0,f100 -Q64 -d425 -M600 -ftargets.dat > ${TS}_Q64_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q64_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q64_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q64_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q64_R70_W30_B16k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b32k -%100:r70,w30,x0,f100 -Q64 -d425 -M600 -ftargets.dat > ${TS}_Q64_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q64_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q64_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q64_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q64_R70_W30_B32k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b64k -%100:r70,w30,x0,f100 -Q64 -d425 -M600 -ftargets.dat > ${TS}_Q64_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q64_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q64_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q64_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q64_R70_W30_B64k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv
logman_start
TS=`date +%y%m%d%H%M%S`
echo >/tmp/.maim_test_start
echo >/tmp/.maim_test_running
maim --perf-mode --latency-histogram=50u,100u,200u,500u,1m,2m,5m,10m,15m,20m,30m,50m,100m,200m,500m,1s,2s,4.7s,5s,10s --full-device -x0u -t10p -b128k -%100:r70,w30,x0,f100 -Q64 -d425 -M600 -ftargets.dat > ${TS}_Q64_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.out
rm -rf /tmp/.maim_test_running
mv `uname -n`.csv  ${TS}_Q64_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.csv
mv `uname -n`.log  ${TS}_Q64_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.log
mv `uname -n`.prf  ${TS}_Q64_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`.prf
logman_stop
mv Run*.csv  ${TS}_Q64_R70_W30_B128k_X0_F100_D420_FC_Phase2_DISRUPTION_`uname -n`_CPU.csv

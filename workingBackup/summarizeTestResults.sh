#
## COpy the files to appropriate directories
#

HOME=`pwd`
DATE_TIME=`date +%y%m%d%H%m%S`
TOTAL_SUMMARY_FILE="${HOME}/total_summary_${DATE_TIME}.csv"

#
## create .testType file in each directory to tag each run - .testType will have Interface (FC/iSCSI), Phase (Phase 1 or 2), test type (normal/congestion)
#

echo "Time Stamp, I/F, Phase, xVal, fVal, Size, Q-Depth, Read, Write, SD:IOPS, SD:MB/S, SD:IO Completion Time, MN:IOPS, MN:MB/S, MN:IO Completion Time, 100th:IOPS, 100th:MB/S, 100th:IO Completion Time, tag" > ${TOTAL_SUMMARY_FILE}

if ls 1707*meanStdDevOut.csv &> /dev/null; then
	for f in 1707*meanStdDevOut.csv
	do
		fprefix=`basename $f .csv`
		tech=`echo $fprefix | awk -F '_' '{ print $9}'`
		phase=`echo $fprefix | awk -F '_' '{ print $10}'`
		tag=`echo $fprefix | awk -F '_' '{ print $11}'`
		xVal=`echo $fprefix | awk -F '_' '{ print $6}'`
		fVal=`echo $fprefix | awk -F '_' '{ print $7}'`
		time_stamp=`echo $fprefix | awk -F '_' '{ print $1}'`
		sed {'1,2d'} ${f}> /tmp/tekPha_temp1 
		echo "${time_stamp}, ${tech}, ${phase}, ${xVal}, ${fVal}, " >/tmp/tekPha_temp2
		paste /tmp/tekPha_temp2 /tmp/tekPha_temp1 | tr -d '\t\r\n' > /tmp/tekPha_temp3
		cat /tmp/tekPha_temp3 >> ${TOTAL_SUMMARY_FILE}
		echo ", $tag">> ${TOTAL_SUMMARY_FILE}
	done
fi
cd $HOME
touch ${TOTAL_SUMMARY_FILE}

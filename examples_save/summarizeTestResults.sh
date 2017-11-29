#
## COpy the files to appropriate directories
#

HOME=`pwd`
DATE_TIME=`date +%y%m%d%H%m%S`
TOTAL_SUMMARY_FILE="${HOME}/total_summary_${DATE_TIME}.csv"

#
## create .testType file in each directory to tag each run - .testType will have Interface (FC/iSCSI), Phase (Phase 1 or 2), test type (normal/congestion)
#

echo "Time Stamp, I/F, Phase, Size, Q-Depth, Read, Write, SD:IOPS, SD:MB/S, SD:IO Completion Time, MN:IOPS, MN:MB/S, MN:IO Completion Time, 100th:IOPS, 100th:MB/S, 100th:IO Completion Time, tag" > ${TOTAL_SUMMARY_FILE}

python copyToTestPhase.py

for d in 1706*
do
	cd $d
	if ls Q*meanStdDevOut.csv &> /dev/null; then
		for f in Q*meanStdDevOut.csv
		do
			fprefix=`basename $f .csv`
			tech=`awk -F ':' '{ print $1}' .testtype`
			phase=`awk -F ':' '{ print $2}' .testtype`
			tag=`awk -F ':' '{ print $3}' .testtype`
			time_stamp=${d}
			cat ${f} | sed {'/^At/d;/^1706/d;/^Size,/d'} > /tmp/tekPha_temp1 
			echo "${time_stamp}, ${tech}, ${phase}, " >/tmp/tekPha_temp2
			paste /tmp/tekPha_temp2 /tmp/tekPha_temp1 | tr -d '\t\r\n' > /tmp/tekPha_temp3
			cat /tmp/tekPha_temp3 >> ${TOTAL_SUMMARY_FILE}
			echo ", $tag">> ${TOTAL_SUMMARY_FILE}

	#		out="${time_stamp}_${tech}_${phase}_${fprefix}.csv"
	#		echo $d
	#		echo $f
	#		echo $out
	#		echo $tag $phase $tech $time_stamp
	#		echo "Time Stamp, I/F, Phase, Size, Q-Depth, Read, Write, SD:IOPS, SD:MB/S, SD:IO Completion Time,\
	#		MN:IOPS, MN:MB/S, MN:IO Completion Time, tag" >/tmp/temp_header
	#		cat /tmp/temp_header /tmp/tekPha_temp3 > ${out}
	#		echo ", $tag">> ${out}
	#		cat ${out}
	#		cat ${out} >> ${TOTAL_SUMMARY_FILE}

		done
	fi
	cd $HOME
done
touch ${TOTAL_SUMMARY_FILE}

#
# driver for calc_average_cpu_perf.py
# just run the script without any arguments
# bug: hardcode "17*_CPU.csv" 
# when the year changes, this string should change
# e.g. for 2018 year should change to 18*_CPU.csv
#

PYSCRIPT="C:\Users\nsomayaj\Box_Sync\BroadcomTransition\SolutionIdeas\FC_iSCSI_Comparison\scripts\perfmon"
TOTAL_SUMMARY_FILENAME=$1

for i in 17*_CPU.csv
do
	f=`basename $i .csv`
	out="${f}_Info.csv"
	echo "${i}: "
	python ${PYSCRIPT}/calc_average_cpu_perf.py $i >$out
done
#DEBUG
echo "calc_average_cpu_perf done"
#read a
#DEBUG
for i in 17*_CPU_Info.csv
do
	f=`basename $i _Info.csv`
	out="${f}_Av_Stats.csv"
	echo "${i}: "
	python ${PYSCRIPT}/get_average_cpu_stats.py $i >$out
done
#DEBUG
echo "calc_average_cpu_perf done"
#read a
#DEBUG
header="Time Stamp,I/F,Phase,xVal,fVal,Size,Q-Depth,Read,Write,tag,Time,CPU % Idle Time,CPU % Intr Time,CPU % Privileged Time,CPU % Proc Time,CPU % User Time" 
out=total_summary_cpu_stats_`date +%y%m%d%H%M%S`.csv

echo $header > $out
for i in 17*_CPU_Av_Stats.csv
do
	grep -v "^Time Stamp," $i  >> $out
done

#add ,(comma) before first column of cpu stats file 
sed -i 's/^/, /g' $out

#now join total summary file that is obtained from Medusa output data and CPU stat data
paste ${TOTAL_SUMMARY_FILENAME} $out > total_summary_io_cpu_stats_`date +%y%m%d%H%M%S`.csv

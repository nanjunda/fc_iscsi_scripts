#
# driver for calc_average_cpu_perf.py
# just run the script without any arguments
# bug: hardcode "17*_CPU.csv" 
# when the year changes, this string should change
# e.g. for 2018 year should change to 18*_CPU.csv
#

PYSCRIPT="C:\Users\nsomayaj\Box_Sync\BroadcomTransition\SolutionIdeas\FC_iSCSI_Comparison\scripts\perfmon"

for i in 17*_CPU.csv
do
	f=`basename $i .csv`
	out="${f}_Info.csv"
	python ${PYSCRIPT}/calc_average_cpu_perf.py $i >$out
done

for i in 17*_CPU_Info.csv
do
	f=`basename $i _Info.csv`
	out="${f}_Av_Stats.csv"
	python ${PYSCRIPT}/get_average_cpu_stats.py $i >$out
done

header="Time Stamp, I/F, Phase, xVal, fVal, Size, Q-Depth, Read, Write, tag, Time, CPU % Idle Time, CPU % Intr Time, CPU % Privileged Time, CPU % Proc Time, CPU % User Time" 
out=`date +%y%m%d%H%M%S`_total_summary_cpu_stats.csv

echo $header > $out
for i in 17*_CPU_Av_Stats.csv
do
	grep -v "^Time Stamp," $i  >> $out
done

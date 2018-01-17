PYSCRIPT="/cygdrive/C/Users/nsomayaj/Box_Sync/BroadcomTransition/SolutionIdeas/FC_iSCSI_Comparison/scripts"
SPREADSHEET_PYSCRIPT="${PYSCRIPT}/spreadsheet"
MEDUSATESTS_PYSCRIPT="${PYSCRIPT}/medusaTests"
PERFMON_PYSCRIPT=${PYSCRIPT}/perfmon
FILENAME_MANIPULATOR_PYSCRIPT=${PYSCRIPT}/filename_manipulator

# pass one of the following  as an argument to this script
#will be called to shorten the filename based on disruption type
#
#"none" -> shortFileName_None.sh
#"port -> shortFileName_Port.sh
#"switch" -> shortFileName_Switch.sh
#
# second argument is output of "uname -n" which is system name e.g. WIN-RVTI38O0S48
# third argument is number of seconds that single test runs. for example, the single run for normal phase1 
# protocol test is 120 seconds whereas for switch reboot disruption is 900 seconds.

PREFIX=17

echo
ls  ${MEDUSATESTS_PYSCRIPT}/calcMeanStdDev.sh  ${MEDUSATESTS_PYSCRIPT}/summarizeTestResults.sh ${PERFMON_PYSCRIPT}/process_perfmon_csv.sh  ${SPREADSHEET_PYSCRIPT}/generate_one_line_graph_per_chart.py ${SPREADSHEET_PYSCRIPT}/eg2_params.json ${SPREADSHEET_PYSCRIPT}/sub_pd_pivot.py
echo

if [ $1 == "none" ]
then
	SHORTEN_FILENAME_SCRIPT="shortFileName_None.sh"
elif [ $1 == "port" ]
then
	SHORTEN_FILENAME_SCRIPT="shortFileName_Port.sh"

elif [ $1 == "switch" ]
then
	SHORTEN_FILENAME_SCRIPT="shortFileName_Switch.sh"

fi

UNAME=$2; export UNAME
single_line_run_time=$3

echo "Calculating mean, SD based mean and 100th entry"
sh ${MEDUSATESTS_PYSCRIPT}/calcMeanStdDev.sh
echo "Summarizing  results"
sh ${MEDUSATESTS_PYSCRIPT}/summarizeTestResults.sh
echo "Processing Perfmon data"
sh ${PERFMON_PYSCRIPT}/process_perfmon_csv.sh total_summary_17*.csv
current_wd=`pwd`
echo "Generating charts based on individual CSV files output by maim"
mkdir charts
cp -rp ${PREFIX}*${UNAME}.csv charts
cd charts
python ${SPREADSHEET_PYSCRIPT}/generate_one_line_graph_per_chart.py '*.csv' $single_line_run_time
sh ${FILENAME_MANIPULATOR_PYSCRIPT}/${SHORTEN_FILENAME_SCRIPT} ${PREFIX}
echo "Generating charts using summarized results"
cd $current_wd
cp -rp ${SPREADSHEET_PYSCRIPT}/eg2_params.json .
python ${SPREADSHEET_PYSCRIPT}/sub_pd_pivot.py total_summary_io_cpu_stats_*.csv eg2_params.json 

# -generateMedusaScripts.sh- coding: utf-8 -*-
# arguments - FC directory, iSCSI directory and Test Type (NORMAL, CONGESTION, DISRUPTION)
#Created on Fri Sep 15 13:02:54 2017
#
#@author: nsomayaj
#

PYSCRIPT="C:\Users\nsomayaj\Box_Sync\BroadcomTransition\SolutionIdeas\FC_iSCSI_Comparison\scripts\medusaTests\generate"

QDEPTH="8-64"
BUFFER_SIZE="8k-128k"
READ_PERCENT_RANGE="100-70-50-0"
INTERVAL="120"

if [ $# -ne 2 ]
then
	echo "$0: $0 <FC Run Directory> <iSCSI Run Directory>"
	exit 1
fi

echo "Start: Generate Phase 1 (Protocol) Medusa Scripts in"
echo "Scripts: FC in $1 iSCSI in $2"
cd $1
echo "FC specific scripts"

python ${PYSCRIPT}/generateMedusaScripts.py FC Phase1 NORMAL targets.dat 0 100 ${INTERVAL} 10p ${QDEPTH} ${BUFFER_SIZE} ${READ_PERCENT_RANGE} > F100_FC_Phase1_D${INTERVAL}
cp ${PYSCRIPT}/fc_targets.dat .
cd ..
cd $2
cp ${PYSCRIPT}/iscsi_targets.dat .
echo "iSCSI specific scripts"
python ${PYSCRIPT}/generateMedusaScripts.py iSCSI Phase1 NORMAL targets.dat 0 100 ${INTERVAL} 10p ${QDEPTH} ${BUFFER_SIZE} ${READ_PERCENT_RANGE} > F100_iSCSI_Phase1_D${INTERVAL}
cd ..
echo "End: Generate Medusa Scripts"

# -generateMedusaScripts.sh- coding: utf-8 -*-
# arguments - FC directory, iSCSI directory and Test Type (NORMAL, CONGESTION, DISRUPTION)
#Created on Fri Sep 15 13:02:54 2017
#
#@author: nsomayaj
#

PYSCRIPT="C:\Users\nsomayaj\Box_Sync\BroadcomTransition\SolutionIdeas\FC_iSCSI_Comparison\scripts\medusaTests\generate"

QDEPTH="1-512"
BUFFER_SIZE="512b-1m"
READ_PERCENT_RANGE="100-70-50-0"
INTERVAL="120"

TEMPLATE_DIR=${PYSCRIPT}/templates
FC_SCRIPT_FILE=F100_FC_Phase1_D${INTERVAL}
iSCSI_SCRIPT_FILE=F100_iSCSI_Phase1_D${INTERVAL}

if [ $# -ne 2 ]
then
	echo "$0: $0 <FC Run Directory> <iSCSI Run Directory>"
	exit 1
fi

echo "Start: Generate Phase 1 (Protocol) Medusa Scripts in"
echo "Scripts: FC in $1 iSCSI in $2"
cd $1
echo "FC specific scripts"

cat ${TEMPLATE_DIR}/logman.template > ${FC_SCRIPT_FILE}
python ${PYSCRIPT}/generateMedusaScripts.py FC Phase1 NORMAL targets.dat 0 100 ${INTERVAL} 10p ${QDEPTH} ${BUFFER_SIZE} ${READ_PERCENT_RANGE} >> ${FC_SCRIPT_FILE}
d2u ${FC_SCRIPT_FILE}
cp ${TEMPLATE_DIR}/fc_targets.dat targets.dat
cd ..
cd $2
cp ${TEMPLATE_DIR}/iscsi_targets.dat targets.dat
echo "iSCSI specific scripts"

cat ${TEMPLATE_DIR}/logman.template > ${iSCSI_SCRIPT_FILE}
python ${PYSCRIPT}/generateMedusaScripts.py iSCSI Phase1 NORMAL targets.dat 0 100 ${INTERVAL} 10p ${QDEPTH} ${BUFFER_SIZE} ${READ_PERCENT_RANGE} >> ${iSCSI_SCRIPT_FILE}
d2u ${iSCSI_SCRIPT_FILE}
cd ..
echo "End: Generate Medusa Scripts"

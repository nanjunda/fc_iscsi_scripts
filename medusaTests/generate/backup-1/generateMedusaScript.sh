# -generateMedusaScripts.sh- coding: utf-8 -*-
# arguments - FC directory, iSCSI directory and Test Type (NORMAL, CONGESTION, DISRUPTION)
#Created on Fri Sep 15 13:02:54 2017
#
#@author: nsomayaj
#

PYSCRIPT="C:\Users\nsomayaj\Box_Sync\BroadcomTransition\SolutionIdeas\FC_iSCSI_Comparison\scripts\medusaTests\generate"
TEMPLATE_DIR=${PYSCRIPT}/templates
FC_SCRIPT_FILE=F100_FC_D480_R70_W30
iSCSI_SCRIPT_FILE=F100_iSCSI_D480_R70_W30

if [ $# -ne 3 ]
then
	echo "$0: $0 <FC Run Directory> <iSCSI Run Directory> TestType"
	exit 1
fi
echo "Start: Generate Medusa Scripts"
TESTTYPE=$3
cd $1
echo "FC specific medusa scripts"
cat ${TEMPLATE_DIR}/logman.template > ${FC_SCRIPT_FILE}
python ${PYSCRIPT}/generateMedusaScripts.py FC Phase2 ${TESTTYPE} targets.dat 0 100 480 10p 8-64 8k-128k 70 >> ${FC_SCRIPT_FILE}
d2u ${FC_SCRIPT_FILE}
cp ${TEMPLATE_DIR}/fc_targets.dat targets.dat

cd ..
cd $2
echo "iSCSI specific medusa scripts"
cat ${TEMPLATE_DIR}/logman.template > ${iSCSI_SCRIPT_FILE}
python ${PYSCRIPT}/generateMedusaScripts.py iSCSI Phase2 ${TESTTYPE} targets.dat 0 100 480 10p 8-64 8k-128k 70 >> ${iSCSI_SCRIPT_FILE} 
d2u ${iSCSI_SCRIPT_FILE} 
cp ${TEMPLATE_DIR}/iscsi_targets.dat targets.dat

cd ..
echo "End: Generate Medusa Scripts"

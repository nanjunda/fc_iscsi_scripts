# -generateMedusaScripts.sh- coding: utf-8 -*-
#
#Created on Fri Sep 15 13:02:54 2017
#
#@author: nsomayaj
#

PYSCRIPT="C:\Users\nsomayaj\Box_Sync\BroadcomTransition\SolutionIdeas\FC_iSCSI_Comparison\scripts\medusaTests"

if [ $# -ne 3 ]
then
	echo "$0: $0 <FC Run Directory> <iSCSI Run Directory> TestType"
	exit 1
fi
echo "Start: Generate Medusa Scripts"
TESTTYPE=$3
cd $1
echo "FC specific medusa scripts"
python ${PYSCRIPT}/generateMedusaScripts.py FC Phase2 ${TESTTYPE} fc_targets.dat 0 100 240 10p  > F100_FC_Q16_B8K
cp ${PYSCRIPT}/fc_targets.dat .
cd ..
cd $2
cp ${PYSCRIPT}/iscsi_targets.dat .
echo "iSCSI specific medusa scripts"
python ${PYSCRIPT}/generateMedusaScripts.py iSCSI Phase2 ${TESTTYPE} iscsi_targets.dat 0 100 240 10p > F100_iSCSI_Q16_B8K
cd ..
echo "End: Generate Medusa Scripts"

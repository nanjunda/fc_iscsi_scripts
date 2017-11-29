#
# shell script to drive combineSummaryCSV.py
# uses sed to add , at end of each of FC summary file (-i option write back)
# uses paste to do columnar join of FC and iSCSI total summary file
# Note that order - FC and iSCSI
# fixes CRLF issue by running d2u on output file from paste commmand
# runs the python script - combineSummaryCSV.py
# this script has three args: FC Summary File name, iSCSI Summary name, and
# new file name for combined FC and iSCSI files
# 
PYSCRIPT="C:\Users\nsomayaj\Box_Sync\BroadcomTransition\SolutionIdeas\FC_iSCSI_Comparison\scripts\pyScript"
PASTEOUT="Paste_${3}"
sed -i '/^17/s/$/,/' $1 
paste $1 $2 >${PASTEOUT}
d2u ${PASTEOUT}
python ${PYSCRIPT}/combineSummaryCSV.py $PASTEOUT $3
d2u $3

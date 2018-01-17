#
# Use the python script - sanSwitchPortManipulate.py to enable or disable switch port
# this script will timestamp when the command was issued and when the command exits
# var1 - between disabling and enabling of the port, wait for var1 secs (short time)
# var2 - once port is disabled and enabled, sleep for var2 secs (longer time)
# var1 and var2 are random numbers between the range of 9 to 19 and 30 to 400
# this loop goes on for ever until is is cancelled using "CONTROL-C"
#

PYSCRIPT="C:\Users\nsomayaj\Box_Sync\BroadcomTransition\SolutionIdeas\FC_iSCSI_Comparison\scripts\sanSwitch"
SERVER_SWITCH_6510="10.26.3.194"
STORAGE_SWITCH_6510="10.26.2.207"
FLOWNAME_1="flowcase1"
FLOWNAME_2="flowcase2"
FLOWNAME_3="flowcase3"
FLOWNAME_4="flowcase4"
FRAME_SIZE=2000

DATE_TIME=`date +%y%m%d%H%m%S`

python ${PYSCRIPT}/sanSwitchSimPort.py ${STORAGE_SWITCH_6510} admin password ${FLOWNAME_3} ${FRAME_SIZE}
python ${PYSCRIPT}/sanSwitchSimPort.py ${SERVER_SWITCH_6510} admin password ${FLOWNAME_2} ${FRAME_SIZE}
python ${PYSCRIPT}/sanSwitchSimPort.py ${SERVER_SWITCH_6510} admin password ${FLOWNAME_4} ${FRAME_SIZE}
python ${PYSCRIPT}/sanSwitchSimPort.py ${STORAGE_SWITCH_6510} admin password ${FLOWNAME_1} ${FRAME_SIZE}

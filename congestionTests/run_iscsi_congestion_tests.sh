#
# 60
#
echo "Start the perfmon"
logman start FC-iSCSI
sleep 60
echo "Starting 60% load"
echo "Check Spirent" 60
read a
echo "Confirm:"
read a
cd Run9_iSCSI_Congestion_60
sh ../F100_iSCSI_R70_W30_Q64_B8K | tee -a 60Out 
cd ..
echo "Stop the perfmon"
sleep 120
logman stop FC-iSCSI

#
# 70
#
echo "Start the perfmon"
logman start FC-iSCSI
sleep 60
echo "Starting 70% load"
echo "Check Spirent 70"
read a
echo "Confirm:"
read a
cd Run9_iSCSI_Congestion_70
sh ../F100_iSCSI_R70_W30_Q64_B8K | tee -a 70Out 
cd ..
echo "Stop the perfmon"
sleep 120
logman stop FC-iSCSI

#
# 80
#
echo "Start the perfmon"
logman start FC-iSCSI
sleep 60
echo "Starting 80% load"
echo "Check Spirent 80"
read a
echo "Confirm:"
read a
cd Run9_iSCSI_Congestion_80
sh ../F100_iSCSI_R70_W30_Q64_B8K | tee -a 80Out 
cd ..
echo "Stop the perfmon"
sleep 120
logman stop FC-iSCSI

#
# 90
#
echo "Start the perfmon"
logman start FC-iSCSI
sleep 60
echo "Starting 90% load"
echo "Check Spirent 90"
read a
echo "Confirm:"
read a
cd Run9_iSCSI_Congestion_90
sh ../F100_iSCSI_R70_W30_Q64_B8K | tee -a 90Out 
cd ..
echo "Stop the perfmon"
sleep 120
logman stop FC-iSCSI

#
# 95
#
echo "Start the perfmon"
logman start FC-iSCSI
sleep 60
echo "Starting 95% load"
echo "Check Spirent 95"
read a
echo "Confirm:"
read a
cd Run9_iSCSI_Congestion_95
sh ../F100_iSCSI_R70_W30_Q64_B8K | tee -a 95Out 
cd ..
echo "Stop the perfmon"
sleep 120
logman stop FC-iSCSI

#
# 100
#
echo "Start the perfmon"
logman start FC-iSCSI
sleep 60
echo "Starting 100% load"
echo "Check Spirent 100"
read a
echo "Confirm:"
read a
cd Run9_iSCSI_Congestion_100
sh ../F100_iSCSI_R70_W30_Q64_B8K | tee -a 100Out 
cd ..
echo "Stop the perfmon"
sleep 120
logman stop FC-iSCSI

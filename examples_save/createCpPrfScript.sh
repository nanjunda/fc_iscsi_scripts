find Test\ History/ -depth -name WIN-H4HNI7DSO7P.prf -print | sed 's/^/cp "/g' | sed 's/$/"/g' >firstColumn.txt
/cygdrive/c/Users/nsomayaj/Box\ Sync/BroadcomTransition/Solution\ Ideas/FC_iSCSI_Comparison/scripts/extractprf.sh > secondColumn.txt
paste firstcolumn.txt secondcolumn.txt


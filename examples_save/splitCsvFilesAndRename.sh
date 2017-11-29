#
#
# this script will will split the CSV file to individual CSV files to a number of CSV files with 120 lines mapping to separate each thread run by 
# medusa. it will also copy 120 line CSV file to a directory, with time stamp as directory name, and names the individual CSV file as follows:
# Q depth, read percentage, read buffer size, write percentage, write buffer size eg. Q64_r100_512b_w0_512b.csv  
#
#
HOME=`pwd`
SCRIPT_DIR=/cygdrive/c/Users/nsomayaj/Box\ Sync/BroadcomTransition/Solution\ Ideas/FC_iSCSI_Comparison/scripts/
mkdir processedFiles
for orgFile in *.csv
do
	dirName=`echo $orgFile | awk -F '_' '{ print $1 }'`
	COPY_TO_DIR=${HOME}/processedFiles/${dirName}
	mkdir $COPY_TO_DIR
	csplit.exe $orgFile /Command\ line:/ {*}
	mv xx* $COPY_TO_DIR
	cd $COPY_TO_DIR
	for i in xx*
	do
		f=`grep 'Command line' $i |  awk -F '-' {'print $14   $13'} | sed 's/,x.*$//g' | awk {'printf("%s%s", $1, $2)'} | sed {'s/[ %,@:]/_/g; s/_100_/_/g'}`
		echo $f $dirName $COPY_TO_DIR $HOME
		sed {'/Command line:/d;/Test Start Time:/d; /--------------/d;/^\r/d'} $i > ${f}.csv
#		python ${SCRIPT_DIR}/pyscript/medusaConvertToArray.py ${f}.csv
		unset f
	done
	cd $HOME 
	unset dirName
	unset COPY_TO_DIR
done

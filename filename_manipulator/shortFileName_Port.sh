LOG_FILE="`date +%y%m%d%H%M%S`_shortFileName.log"
PREFIX=${1}
FILES=${PREFIX}*${UNAME}.xlsx

>${LOG_FILE}
for i in ${FILES}
do
	j=`echo ${i%.*} | awk -F_ '{ printf("%s_%s_%s_%s_P%s.xlsx", $2, $3, $5, $9, $11) }'`
	echo "mv $i $j" >>${LOG_FILE}
	mv $i $j
done
cat $LOG_FILE

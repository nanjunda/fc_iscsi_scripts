LOG_FILE="`date +%y%m%d%H%M%S`_shortFileName.log"
for i in 171014*P.xlsx
do
	j=`echo ${i%.*} | awk -F_ '{ printf("%s_%s_%s_%s%s.xlsx", $2,$5, $9, $11, $12) }'`
	echo "mv $i $j" >${LOG_FILE}
	mv $i $j
done

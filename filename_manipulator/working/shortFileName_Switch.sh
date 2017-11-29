LOG_FILE="`date +%y%m%d%H%M%S`_shortFileName_Switch.log"
for i in 171013*P.xlsx
do
	j=`echo ${i%.*} | awk -F_ '{ printf("%s_%s_%s_S%s.xlsx", $2,$5, $9, $11) }'`
	echo "mv $i $j" >${LOG_FILE}
	mv $i $j
done

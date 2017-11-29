for i in */*.csv
do
	echo $i
	d=`dirname $i`
	f=`basename $i .csv`
	out="${d}/${f}_meanStdDevOut.csv"
#	echo $d
#	echo $f
#	echo $out
	python medusaConvertToArray.py $i > ${out}
done
	echo "Completed mean and SD calucalation"

for i in *.csv
do
	echo $i
	sed {'/Command line:/d;/Test Start Time:/d; /--------------/d;/^\r/d'} $i > tmp.csv
	mv tmp.csv $i
	f=`basename $i .csv`
	out="${f}_meanStdDevOut.csv"
	echo $f
	echo $out
	python medusaConvertToArray.py $i > ${out}
done
	echo "Completed mean and SD calucalation"

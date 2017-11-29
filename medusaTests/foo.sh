echo $#
if [ $# -ne 3 ]
then
	echo "Need 3 arguments"
	exit 1
fi
echo $0
echo $1
echo $2
echo $3

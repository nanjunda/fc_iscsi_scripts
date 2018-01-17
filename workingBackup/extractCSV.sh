#!/bin/sh
TIMESTAMP=`date +%y%m%d%H%M%S`
CSV_DIR="CSV${TIMESTAMP}"

mkdir ${CSV_DIR}
rm /tmp/csvFilesWithPath.txt /tmp/csvFileTimeStamp.txt /tmp/csvFileName.txt /tmp/csvFileNameWithTimeStamp.txt

find . -depth -name WIN-H4HNI7DSO7P.csv -print >/tmp/csvFilesWithPath.txt
grep -oh '1706[0-9]*/w' /tmp/csvFilesWithPath.txt | sed 's:/w::g'>/tmp/csvFileTimeStamp.txt
sed {'s/Single Initiator-Single Target[ ,a-z,A-Z,0-9]*//g; s/win-h4hni7dso7p (10.26.2.162)//g; s:1706[0-9,/]*::g; s/ WIN/_WIN/g; s:^\./::g; s/-/_/g; s:Test History/::g; s/ /_/g; s/__/_/g'} /tmp/csvFilesWithPath.txt  > /tmp/csvFileName.txt
paste /tmp/csvFileTimeStamp.txt /tmp/csvFileName.txt  | sed {"s/\t/_/g; s:^:\"CSV${TIMESTAMP}/:g; s/$/\"/g"} >/tmp/csvFileNameWithTimeStamp.txt

cat /tmp/csvFileNameWithTimeStamp.txt

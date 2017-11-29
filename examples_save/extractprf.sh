#!/bin/sh
TIMESTAMP=`date +%y%m%d%H%M%S`
PRF_DIR="PRF${TIMESTAMP}"

mkdir ${PRF_DIR}
rm /tmp/prfFilesWithPath.txt /tmp/prfFileTimeStamp.txt /tmp/prfFileName.txt /tmp/prfFileNameWithTimeStamp.txt

find . -depth -name WIN-H4HNI7DSO7P.prf -print >/tmp/prfFilesWithPath.txt
grep -oh '1706[0-9]*/w' /tmp/prfFilesWithPath.txt | sed 's:/w::g'>/tmp/prfFileTimeStamp.txt
sed {'s/Single Initiator-Single Target[ ,a-z,A-Z,0-9]*//g; s/win-h4hni7dso7p (10.26.2.162)//g; s:1706[0-9,/]*::g; s/ WIN/_WIN/g; s:^\./::g; s/-/_/g; s:Test History/::g; s/ /_/g; s/__/_/g'} /tmp/prfFilesWithPath.txt  > /tmp/prfFileName.txt
paste /tmp/prfFileTimeStamp.txt /tmp/prfFileName.txt  | sed {"s/\t/_/g; s:^:\"PRF${TIMESTAMP}/:g; s/$/\"/g"} >/tmp/prfFileNameWithTimeStamp.txt

cat /tmp/prfFileNameWithTimeStamp.txt

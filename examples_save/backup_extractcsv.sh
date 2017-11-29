#!/bin/sh
find . -depth -name WIN-H4HNI7DSO7P.csv -print | sed 's/Single Initiator-Single Target[ ,a-z,A-Z,0-9]*//g' | sed 's/win-h4hni7dso7p (10.26.2.162)//g' | sed 's:1706[0-9,/]*::g' | sed 's/ WIN/_WIN/g' | sed 's:^\./::g' | sed 's/-/_/g' > /tmp/filename.txt
while read line; do echo $line | sed 's/ /_/g' | sed 's/Test_H/Test H/g' | sed 's/__/_/g'; done </tmp/filename.txt >/tmp/foo
while read line; do echo $line | sed 's/^/"/g' | sed 's/$/"/g' | sed 's:Test History/:Test History/CSV/:g'; done </tmp/foo >/tmp/foo1
n=1; while read line; do echo $line | sed "s/WIN_H4HNI7DSO7P/WIN_H4HNI7DSO7P_${n}/"; n=$((++n)); done </tmp/foo1


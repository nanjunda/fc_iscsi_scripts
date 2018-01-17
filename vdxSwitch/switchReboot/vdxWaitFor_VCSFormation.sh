#!/bin/bash

SWITCH_IP=$1
SWITCH_ADMIN=$2
SWITCH_PASSWD=$3

output=`/usr/bin/expect << EOD
spawn ssh $SWITCH_ADMIN@$SWITCH_IP
expect "*# "
send  "sh vcs\r"
expect "*# "
puts "\$expect_out"
EOD`

echo $output

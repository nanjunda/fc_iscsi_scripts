#!/bin/bash

SWITCH_IP=$1
SWITCH_ADMIN=$2
SWITCH_PASSWD=$3

/usr/bin/expect << EOD
spawn ssh $SWITCH_ADMIN@$SWITCH_IP
expect *assword:*
send -- "$SWITCH_PASSWD\r" 
expect "*# "
send -- "\r"
expect "*# "
send -- "fastboot\r"
expect "Are you sure you want to fastboot the switch? \[y/n\]:"
send -- "y\r"
EOD

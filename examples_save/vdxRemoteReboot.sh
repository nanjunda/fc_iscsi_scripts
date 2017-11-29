#!/bin/bash

PWD="password"

rm -rf /tmp/.vdx_switch_ready
/usr/bin/expect << EOD
spawn ssh admin@10.26.3.161
expect *assword:*
send -- "$PWD\r" 
expect "*# "
send -- "\r"
expect "*# "
send -- "fastboot\r"
expect "Are you sure you want to fastboot the switch? \[y/n\]:"
send -- "y\r"
expect -- 'rejoined VCS cluster.'
puts " The output is \$expect_out(buffer) "
EOD
echo >/tmp/.vdx_switch_ready

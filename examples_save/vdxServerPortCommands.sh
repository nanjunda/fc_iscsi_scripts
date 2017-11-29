#!/bin/bash

PWD="password"

interface_type=fo
interface_type_te=te

int1="sh int te 12/0/22"

int2="sh int te 13/0/22"


rm -rf /tmp/.vdx_switch_ready
/usr/bin/expect << EOD
spawn ssh admin@10.26.2.57
expect *assword:*
send -- "$PWD\r" 
expect "*# "
send -- "\r"
expect "*# "

send -- "$int1 | exc more\r"
expect "*# "
send -- "$int2 | exc more\r"
expect "*# "
#puts " The output is \$expect_out(buffer) "
EOD

#!/bin/bash

PWD="password"
interface_type=fo
interface_type_te=te
int1="sh int te 12/0/38"
int2="sh int te 12/0/39"
int3="sh int te 12/0/40"
int4="sh int te 12/0/42"
int5="sh int te 12/0/43"
int6="sh int te 12/0/44"
int7="sh int te 12/0/45"
int1="sh int te 12/0/46"

int8="sh int te 13/0/40"
int9="sh int te 13/0/42"
inta="sh int te 13/0/44"
intb="sh int te 13/0/46"
intc="sh int fo 13/0/51"


rm -rf /tmp/.vdx_switch_ready
/usr/bin/expect << EOD
spawn ssh admin@10.26.3.161
expect *assword:*
send -- "$PWD\r" 
expect "*# "
send -- "\r"
expect "*# "

send -- "$int1 | exc more\r"
expect "*# "
send -- "$int2 | exc more\r"
expect "*# "
send -- "$int3 | exc more\r"
expect "*# "
send -- "$int4 | exc more\r"
expect "*# "
send -- "$int5 | exc more\r"
expect "*# "
send -- "$int6 | exc more\r"
expect "*# "
send -- "$int7 | exc more\r"
expect "*# "
send -- "$int8 | exc more\r"
expect "*# "
send -- "$int9 | exc more\r"
expect "*# "
send -- "$inta | exc more\r"
expect "*# "
send -- "$intb | exc more\r"
expect "*# "
send -- "$intc | exc more\r"
expect "*# "
#puts " The output is \$expect_out(buffer) "
EOD

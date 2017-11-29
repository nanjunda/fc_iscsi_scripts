#!/bin/bash

PWD="password"
interface_type=fo
interface1=12/0/49
interface2=12/0/50
interface3=13/0/49
interface4=13/0/50
interface_type_te=te
interface5=12/0/1
interface6=13/0/47
interface6=13/0/48

interface7=13/0/22
interface8=12/0/22

rm -rf /tmp/.vdx_switch_ready
/usr/bin/expect << EOD
spawn ssh admin@10.26.3.161
expect *assword:*
send -- "$PWD\r" 
expect "*# "
send -- "\r"
expect "*# "

send -- "sh int $interface_type $interface1 | exc more\r"
expect "*# "
send -- "sh int $interface_type $interface2 | exc more\r"
expect "*# "
send -- "sh int $interface_type $interface3 | exc more\r"
expect "*# "
send -- "sh int $interface_type $interface4 | exc more\r"
expect "*# "
send -- "sh int $interface_type_te $interface5 | exc more\r"
expect "*# "
send -- "sh int $interface_type_te $interface6 | exc more\r"
expect "*# "
send -- "sh int $interface_type_te $interface7 | exc more\r"
expect "*# "
send -- "sh int $interface_type_te $interface8 | exc more\r"
expect "*# "
#puts " The output is \$expect_out(buffer) "
EOD

#!/bin/bash

PWD="password"
interface_type=fo
interface1=14/0/49
interface2=14/0/50
interface3=11/0/49
interface4=11/0/50
interface_type_te=te
interface5=14/0/1
interface6=14/0/47
interface6=14/0/48


interface7=14/0/21
interface8=14/0/22
interface9=11/0/21
interfacea=11/0/22

rm -rf /tmp/.vdx_switch_ready
/usr/bin/expect << EOD
spawn ssh admin@10.26.2.98
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
send -- "sh int $interface_type_te $interface9 | exc more\r"
expect "*# "
send -- "sh int $interface_type_te $interfacea | exc more\r"
expect "*# "
#puts " The output is \$expect_out(buffer) "
EOD

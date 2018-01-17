#
# this shell script takes executable file or script file as the input
# prefixes date and time to file name, removes the extension and
# redirects the output to that file
#
rm -rf /tmp/.maim_test_start /tmp/.maim_test_running
out=`basename ${1} ".py"`.out
echo "$1 >`date +%y%m%d%H%M%S`_${out} 2>&1"
python $1 >`date +%y%m%d%H%M%S`_${out} 2>&1

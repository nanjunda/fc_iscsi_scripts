for i in PRF170627231700/*.prf
do
OUTPUT_FILE="PRF170627231700/CSV/`basename $i .prf`.csv"

sed {'/^\[CPU\]/q; s/\t//g'} $i  | grep -v 'Command Line' | grep -v '^\[' | cut -d'=' -f1 | tr '[\r\n]' '[ ,]' | sed {'s/,$/\n/'} >$OUTPUT_FILE
sed {'/^\[CPU\]/q; s/\t//g'} $i  | grep -v 'Command Line' | grep -v '^\[' | cut -d'=' -f2 | tr '[\r\n]' '[ ,]' | sed {'s/,$/\n/'} >>$OUTPUT_FILE
cat $OUTPUT_FILE
echo
done

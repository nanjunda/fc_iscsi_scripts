#
# this python script generated pivot table based on CSV files generated
# by maim in Congestion and Disruption tests
# in these tests, only one read percentage value of 70% is used
# with IO buffer sizes of 4K to 128K and Queue Depth of 8 through 64
# in other only partial paramaeters are used. On the other hand,
# in full fledged tests (phase 1 tests), the values are:
# for read % of 100, 70, 50, 0; IO buffer size of 512, 1k, 2k, 4k, 8k, 16k, 32k, 64k, 128k, 256k, 512k
# and queue depth of 1, 2, 4, 8, 16, 32, 64, 128, 256, 512 are used
#



import pandas as pd
import numpy as np
import sys
import os
import json


def pivot_table_qd_compare(cat, indx, col, val, new_col1, new_col2, tab_titl, sheet_name):
	# read_pct=[70]
	# size_vals=[4096,8192,16384,32768,65536,131072]
	# qdepth_vals=[8,16,32,64]

	i=0
	c=1
	r=5
	num_rd_pct = len(read_pct)

	while i < num_rd_pct:
		df31 = df3[df3[cat] == read_pct[i]]
		table = df31.pivot(index=indx, columns=col, values=val)
		s=0
		for qd in qdepth_vals:
			s += table[qd]
		table[new_col1] = s/len(qdepth_vals)
		table[new_col2] = read_pct[i]
		table_title = tab_titl + str(read_pct[i])
		table.to_excel(writer, sheet_name, startcol=c, startrow=r)
		sheet = writer.sheets[sheet_name]
		sheet.write(r-3, c, table_title, title_format)
		r += len(table.index)+6
		i += 1
		print(table)


def load_params_json(json_file, rd_pct, siz, qdepth, cong, disrupt):
	with open(json_file, "r") as f:
		buf = f.read()
	data = json.loads(buf)
	rd_pct = data["read_pct"]
	siz = data["io_size"]
	qdepth = data["que_depth"]
	cong = data["congestion"]
	disrupt = data["disruption"]
#
# main script starts
#
read_pct = []
size_vals = []
qdepth_vals = []
congestion_pct = 0
disrupt_type = "None"

input_csv_file = sys.argv[1]
json_param_file = sys.argv[2]
load_params_json(json_param_file, read_pct, size_vals, qdepth_vals, congestion_pct, disrupt_type)
output_xlsx_file=os.path.splitext(os.path.basename(input_csv_file))[0]+'.xlsx'

print(input_csv_file, output_xlsx_file)


pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# reading the date
df1 = pd.read_csv(input_csv_file, index_col=None)
print(list(df1))
writer = pd.ExcelWriter(output_xlsx_file)
df1.to_excel(writer, 'Total Summary')


df3 = df1[['Size', 'Q-Depth', 'Read', 'SD:IOPS', 'SD:MB/S', 'SD:IO Completion Time', 'CPU % Idle Time', 'CPU % Intr Time', 'CPU % Privileged Time', 'CPU % Proc Time', 'CPU % User Time']]
print(df3)
df3.to_excel(writer, 'Selected Summary')


# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
# Add a header format.
title_format = workbook.add_format({
    'bold': True,
    'text_wrap': False,
    'valign': 'top'
   })

##################################################################
#                                                                #
#                  GENERATE Q-Depth vs IOPS                      #
#                                                                #
##################################################################
i=0
c=1
r=5

cat = 'Read'

indx = 'Size'
col = 'Q-Depth'
val_iops = 'SD:IOPS'

new_col1 = 'Average'
new_col2 = 'RD%'

tab_titl = 'Read Percentage: '
sheet_name_iops = 'QD vs IOPS'

pivot_table_qd_compare(cat, indx, col, val_iops, new_col1, new_col2, tab_titl,sheet_name_iops)


##################################################################
#                                                                #
#                  GENERATE Q-Depth vs ThroughPut                      #
#                                                                #
##################################################################


i=0
c=1
r=5

cat = 'Read'

indx = 'Size'
col = 'Q-Depth'
val_throughput = 'SD:MB/S'

new_col1 = 'Average'
new_col2 = 'RD%'

tab_titl = 'Read Percentage: '
sheet_name_throughput = 'QD vs Throughput'

pivot_table_qd_compare(cat, indx, col, val_throughput, new_col1, new_col2, tab_titl,sheet_name_throughput)



##################################################################
#                                                                #
#                  GENERATE Q-Depth vs Latency                      #
#                                                                #
##################################################################


i=0
c=1
r=5

cat = 'Read'

indx = 'Size'
col = 'Q-Depth'
val_latency = 'SD:IO Completion Time'

new_col1 = 'Average'
new_col2 = 'RD%'

tab_titl = 'Read Percentage: '
sheet_name_latency = 'QD vs Latency'

pivot_table_qd_compare(cat, indx, col, val_throughput, new_col1, new_col2, tab_titl,sheet_name_latency)


# table = df3.pivot(columns=' Q-Depth', values=' SD:IO Completion Time')
# print(table)
# table.to_excel(writer, 'QD vs Latency')
writer.save()

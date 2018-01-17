import pandas as pd
import numpy as np
import sys
import os


def pivot_table_qd_compare(cat, indx, col, val, new_col1, new_col2, tab_titl, sheet_name):
	read_pct=[100,70,50,0]
	size_vals=[512, 1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576]
	qdepth_vals=[1,2,4,8,16,32,64,128,256,512]

	i=0
	c=1
	r=5

	while i < 4:
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


#
# main script starts
#

input_csv_file = sys.argv[1]
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

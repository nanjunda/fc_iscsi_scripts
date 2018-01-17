
#
# this python script generated pivot table based on CSV files generated
# by maim in protocol  tests (phase 1)
# in full fledged tests (phase 1 tests), the values are:
# for read % of 100, 70, 50, 0; IO buffer size of 512, 1k, 2k, 4k, 8k, 16k, 32k, 64k, 128k, 256k, 512k
# and queue depth of 1, 2, 4, 8, 16, 32, 64, 128, 256, 512 are used
# in gen1 version: it is only queue depth vs IOPS, Throughput, and Latency
# in gen2 version: adding iops vs throughput; iops vs latency; throughput vs latency; throughput vs cpu utilization
# in gen3 version: added chart generation
# in gen4 removed trend line, x-scale in add_line_chart function is changed to 1 from 1.5, order worksheets
#


import pandas as pd
import sys
import os
import collections
import xlsxwriter

#
# this function generates table for  Queue Depth vs IOPS for IO Sizes of 512b, 1k, 2k, 4k, 8k, 16k, 32k, 64k, 128k, 256k, 512k
# per READ percentage of 100, 70, 50 and 0 (implies WRITE percentage of 0, 30, 50, 100)
#

def pivot_table_qd_compare(cat, indx, col, val, new_col1, new_col2, tab_titl, sheet_name):
	read_pct=[100,70,50,0]
	qdepth_vals=[1,2,4,8,16,32,64,128,256,512]


	i=0
	table_column=1
	table_row=5

	while i < 4:
		big_ordered_dict = collections.OrderedDict()
		# select only one READ percentatage at a time (selection of 100,70, 50, 0)
		df31 = df3[df3[cat] == read_pct[i]]
		#create pivot table from filtered data for a given Read percentage
		table = df31.pivot_table(index=indx, columns=col, values=val)
		#now calculate average over all the queue depths for a given IO Size. 
		#IO Size is index for this pivot table
		s=0
		for qd in qdepth_vals:
			s += table[qd]
		table[new_col1] = s/len(qdepth_vals)
		table[new_col2] = read_pct[i]
		table_title = tab_titl + str(read_pct[i])

		big_ordered_dict["Table"] = table
		big_ordered_dict["Table Title"] = table_title
		big_ordered_dict["Table Title Format"] = title_format
		big_ordered_dict["Sheet Name"] = sheet_name
		big_ordered_dict["Column"] = table_column
		big_ordered_dict["Row"] = table_row 
		big_ordered_dict["Title Column"] = table_column
		big_ordered_dict["Title Row"] = table_row-3
		big_list.append(big_ordered_dict)

		table_row += len(table.index)+6
		i += 1
		# print(table)

#
# this function generates ONE table  Queue Depth vs IOPS for IO Sizes of 512b, 1k, 2k, 4k, 8k, 16k, 32k, 64k, 128k, 256k, 512k
# by taking average over  READ percentage of 100, 70, 50 and 0 (implies WRITE percentage of 0, 30, 50, 100)
# we have big dictionary that stores all the things that needs to be written into Excel workbook at the end
# they are: "Table", "Table Title", "Table Title Format", "Title Column", "Title Row", "Sheet Name", "Column", "Row"
#

def pivot_table_qd_compare_all_read(cat, indx, col, val, new_col1, table_title, sheet_name, rd_col, rd_row):
	qdepth_vals=[1,2,4,8,16,32,64,128,256,512]
	big_ordered_dict = collections.OrderedDict()


	df31 = df3
	table = df31.pivot_table(index=indx, columns=col, values=val)
	s=0
	for qd in qdepth_vals:
		s += table[qd]
	table[new_col1] = s/len(qdepth_vals)
	save_avg_tables.append(table)

	big_ordered_dict["Table"] = table
	big_ordered_dict["Table Title"] = table_title
	big_ordered_dict["Table Title Format"] = title_format
	big_ordered_dict["Sheet Name"] = sheet_name
	big_ordered_dict["Column"] = rd_col
	big_ordered_dict["Row"] = rd_row
	big_ordered_dict["Title Column"] = rd_col
	big_ordered_dict["Title Row"] = rd_row-3
	big_avg_list.append(big_ordered_dict)
	# print(table)

#
# write all the saved tables in to appropriate worksheets inside a given workbook
# used big_ordered_dict to get details about table and necessary things to write table 
# in a given workbook
#

def write_tables_workbook():
	for d in big_list:
		d["Table"].to_excel(writer, d["Sheet Name"], startcol=d["Column"], startrow=d["Row"])
		sheet = writer.sheets[d["Sheet Name"]]
		sheet.write(d["Title Row"], d["Title Column"], d["Table Title"], d["Table Title Format"])

	for d in big_avg_list:
		d["Table"].to_excel(writer, d["Sheet Name"], startcol=d["Column"], startrow=d["Row"])
		sheet = writer.sheets[d["Sheet Name"]]
		sheet.write(d["Title Row"], d["Title Column"], d["Table Title"], d["Table Title Format"])
#
# now get onto charts
#

#
# args: wb- workbook; sh: sheet; cn: column name
# sr: start row; er: end row
#
def add_line_chart(wb, ws, dict_array, x_axis_name, y_axis_name, start_cell, chart_title):
# create new chart object
	chart = wb.add_chart({'type': 'line'})

# add following series to the chart
	i = 0
	for d in dict_array:
		chart.add_series(d)
		if i == 0:
			chart.set_x_axis({'name': x_axis_name[i]})
			chart.set_y_axis({'name': y_axis_name[i]})
		else:
			chart.set_y2_axis({'name': y_axis_name[i]})

		i += 1
# insert the chart into the worksheet
	chart.set_title({'name' : chart_title})
	ws.insert_chart(start_cell, chart, {'x_scale': 1, 'y_scale': 1})



#
# main script starts
#

input_csv_file = sys.argv[1]
output_xlsx_file=os.path.splitext(os.path.basename(input_csv_file))[0]+'.xlsx'

# print(input_csv_file, output_xlsx_file)

save_avg_tables = []

#
#save everything about table and where it should be written in worksheet
#in this ordered dictionary  (using collections). We cannot control the written
#order in the regular python diectionary. hence using ordered dictionary from
#collections
#
big_list = []
big_avg_list = []

pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# reading the date
df1 = pd.read_csv(input_csv_file, index_col=None)
# print(list(df1))



writer = pd.ExcelWriter(output_xlsx_file)
df1.to_excel(writer, 'Total Summary')


df3 = df1[['Size', 'Q-Depth', 'Read', 'SD:IOPS', 'SD:MB/S', 'SD:IO Completion Time', 'CPU % Idle Time', 'CPU % Intr Time', 'CPU % Privileged Time', 'CPU % Proc Time', 'CPU % User Time']]
# print(df3)
df3.to_excel(writer, 'Selected Summary')

# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
# Add a header format.
title_format = workbook.add_format({
    'bold': True,
    'text_wrap': False,
    'valign': 'top'
   })

cat = 'Read'
indx = 'Size'
col = 'Q-Depth'
new_col1 = 'Average'
new_col2 = 'RD%'

##################################################################
#                                                                #
#                  GENERATE Q-Depth vs IOPS                      #
#                                                                #
##################################################################
rc=1
rr=5

val = 'SD:IOPS'
tab_titl = 'Read Percentage: '
sheet_name_iops = 'QD vs IOPS'
pivot_table_qd_compare(cat, indx, col, val, new_col1, new_col2, tab_titl,sheet_name_iops)

tab_titl = 'Average IOPS over all RD%'
sheet_name_avg = 'Average Vals'
pivot_table_qd_compare_all_read(cat, indx, col, val, new_col1, tab_titl,sheet_name_avg, rc, rr)
rr += 17

##################################################################
#                                                                #
#                  GENERATE Q-Depth vs ThroughPut                #
#                                                                #
##################################################################

val = 'SD:MB/S'
tab_titl = 'Read Percentage: '
sheet_name_throughput = 'QD vs Throughput'
pivot_table_qd_compare(cat, indx, col, val, new_col1, new_col2, tab_titl,sheet_name_throughput)

tab_titl = 'Average Throughput over all RD%'
sheet_name_avg = 'Average Vals'
pivot_table_qd_compare_all_read(cat, indx, col, val, new_col1, tab_titl,sheet_name_avg, rc, rr)
rr += 17



##################################################################
#                                                                #
#                  GENERATE Q-Depth vs Latency                   #
#                                                                #
##################################################################
c=1
r=5

val = 'SD:IO Completion Time'
new_col1 = 'Average'
new_col2 = 'RD%'
tab_titl = 'Read Percentage: '
sheet_name_latency = 'QD vs Latency'
pivot_table_qd_compare(cat, indx, col, val, new_col1, new_col2, tab_titl,sheet_name_latency)

tab_titl = 'Average Latency over all RD%'
sheet_name_avg = 'Average Vals'
pivot_table_qd_compare_all_read(cat, indx, col, val, new_col1, tab_titl,sheet_name_avg, rc, rr)
rr += 17


##################################################################
#                                                                #
#                  GENERATE Q-Depth vs CPU Utilization           #
#                                                                #
##################################################################
c=1
r=5
val = 'CPU % Proc Time'
new_col1 = 'Average'
new_col2 = 'RD%'
tab_titl = 'Read Percentage: '
sheet_name_cpu_util = 'QD vs CPU Utilization'
pivot_table_qd_compare(cat, indx, col, val, new_col1, new_col2, tab_titl,sheet_name_cpu_util)

tab_titl = 'Average CPU Util over all RD%'
sheet_name_avg = 'Average Vals'
pivot_table_qd_compare_all_read(cat, indx, col, val, new_col1, tab_titl,sheet_name_avg, rc, rr)
rr +=17



##################################################################
#                                                                #
#          GENERATE table of averages against IO Size            #
#                                                                #
##################################################################
key_list = ["IOPS", "Throughput", "Latency", "CPU Utilization"]
ordered_dict = collections.OrderedDict()
i=0
for t in save_avg_tables:
	ordered_dict[key_list[i]] = t["Average"]
	i += 1
df = pd.DataFrame(ordered_dict)
b = collections.OrderedDict()
table_title = "Size vs Averages(IOPS/Throughput/Latency/CPU Utilization)"
sheet_name = "Averages"
rd_col = 1
rd_row = 5

b["Table"] = df
b["Table Title"] = table_title
b["Table Title Format"] = title_format
b["Sheet Name"] = sheet_name
b["Column"] = rd_col
b["Row"] = rd_row
b["Title Column"] = rd_col
b["Title Row"] = rd_row-3
big_avg_list.append(b)
# print(df)
write_tables_workbook()

#
# get onto charting 
#


# create new worksheet by creating empty DataFrame and putting the empty DataFrame in
# new sheet.
df_empty = pd.DataFrame({'A': []})
df_empty.to_excel(writer, sheet_name='Charts')
ws = writer.sheets['Charts']



x_axis_name = []
y_axis_name = []

#
#IO Size vs IOPS & Throughput chart
#
x_axis_name.append('IO Size')
dictarray = [
             {'categories': '=Averages!$B$7:$B$18', 'values': '=Averages!$C$7:$C$18', 'name': '=Averages!$C$6', 
              'line': {'color': 'red'}, 'marker' : {'type' : 'circle'},}, 
             {'categories': '=Averages!$B$7:$B$18', 'values': '=Averages!$D$7:$D$18', 'name': '=Averages!$D$6', 
              'line': {'color': 'blue'}, 'marker' : {'type' : 'circle'},'y2_axis' : 1,}
             ]
y_axis_name.append('IOPS')
y_axis_name.append('Throughput')
chart = add_line_chart(workbook, ws, dictarray, x_axis_name, y_axis_name, 'A1', 'IO Size vs IOPS & Throughput')
y_axis_name.pop()

#
#IO Size vs IOPS & Latency chart
#            
x_axis_name.append('IO Size')
dictarray = [
             {'categories': '=Averages!$B$7:$B$18', 'values': '=Averages!$C$7:$C$18', 'name': '=Averages!$C$6', 
              'line': {'color': 'red'}, 'marker' : {'type' : 'circle'},}, 
             {'categories': '=Averages!$B$7:$B$18', 'values': '=Averages!$E$7:$E$18', 'name': '=Averages!$E$6', 
              'line': {'color': 'green'}, 'marker' : {'type' : 'circle'}, 'y2_axis' : 1,}
            ]
y_axis_name.append('IOPS')
y_axis_name.append('Latency')
chart = add_line_chart(workbook, ws, dictarray, x_axis_name, y_axis_name, 'I1', 'IO Size vs IOPS & Latency')
y_axis_name.pop()

#
#IO Size vs Throughput & Latency chart
#            
x_axis_name.append('IO Size')
dictarray = [
             {'categories': '=Averages!$B$7:$B$18', 'values': '=Averages!$D$7:$D$18', 'name': '=Averages!$D$6',
              'line': {'color': 'blue'}, 'marker' : {'type' : 'circle'},},
             {'categories': '=Averages!$B$7:$B$18', 'values': '=Averages!$E$7:$E$18', 'name': '=Averages!$E$6', 
              'line': {'color': 'green'}, 'marker' : {'type' : 'circle'}, 'y2_axis' : 1,}
            ]
y_axis_name.append('Throughput')
y_axis_name.append('Latency')
chart = add_line_chart(workbook, ws, dictarray, x_axis_name, y_axis_name, 'A16', 'IO Size vs Throughput & Latency')
y_axis_name.pop()

#
#IO Size vs Throughput & CPU Utilization chart
#            
x_axis_name.append('IO Size')
dictarray = [
             {'categories': '=Averages!$B$7:$B$18', 'values': '=Averages!$D$7:$D$18', 'name': '=Averages!$D$6',
              'line': {'color': 'blue'}, 'marker' : {'type' : 'circle'},},
             {'categories': '=Averages!$B$7:$B$18', 'values': '=Averages!$F$7:$F$18', 'name': '=Averages!$F$6', 
              'line': {'color': 'green'}, 'marker' : {'type' : 'circle'}, 'y2_axis' : 1,}
            ]
y_axis_name.append('Throughput')
y_axis_name.append('CPU Util')
chart = add_line_chart(workbook, ws, dictarray, x_axis_name, y_axis_name, 'I16', 'IO Size vs Throughput & CPU Utilization')
y_axis_name.pop()

# order worksheets
ws = writer.sheets['Charts']
ws.set_first_sheet()
ws.activate()
writer.save()
workbook.close()
#NS

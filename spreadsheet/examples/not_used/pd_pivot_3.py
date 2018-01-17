import pandas as pd
import numpy as np
import sys
import os



def csv_to_excel_sheet(df, writer, sheet_name):
	df.to_excel(writer, sheet_name)


def select_summary_sheet(df, column_list, sheet_name):
	df1 = df[column_list]
	df1.to_excel(writer, sheet_name)


#
# generage pivot table, table from given DataFrame, df
# return table
#
def generate_pivot_table(df, sheet_name, cat_name, cat_val, indx, cols, vals):
		df1 = df[df[cat] == cat_val]
		table = df1.pivot(index=indx, columns=col, values=vals)

#
# calculate averate of each row
#
def calc_average_row_value(row_head_list, table):
	s=0
	for qd in row_head_list:
		s += table[qd]
	table["Average"] = s/len(row_head_list)


def write_table_to_sheet(table, writer_handle, titl, titl_format, sheet_name, start_col, start_row):
	table.to_excel(writer, sheet_name, startcol=start_col, startrow=start_row)
	sheet = writer.sheets[sheet_name]
	sheet.write(start_row-3, start_col, titl, titl_format)
	print(table)


#
# main
#

read_pct=[100,70,50,0]
qdepth_vals=[1,2,4,8,16,32,64,128,256,512]


output_xlsx_file=""
my_df=None
writer=None
workbook=None


pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

input_csv_file = sys.argv[1]
output_xlsx_file=os.path.splitext(os.path.basename(input_csv_file))[0]+'.xlsx'
my_df = pd.read_csv(input_csv_file, index_col=None)
writer = pd.ExcelWriter(output_xlsx_file)
workbook  = writer.book

csv_to_excel_sheet(my_df, writer, "Total Summary")
selected_columns = ['Size', 'Q-Depth', 'Read', 'SD:IOPS', 'SD:MB/S', 'SD:IO Completion Time', 'CPU % Idle Time', 'CPU % Intr Time', 'CPU % Privileged Time', 'CPU % Proc Time', 'CPU % User Time']
select_summary_sheet(my_df, selected_columns, "Selected Summary")


i=0
start_col=1
start_row=5

while i < 4:
	pivot_table = generate_pivot_table(my_df, "Read", "Size", "Q-Depth", read_pct[i], "SD:IOPS")
	calc_average_row_value(qdepth_vals, pivot_table)

	table_title = "Read Percentage: " + str(read_pct[i])
	sheet_name = "QD vs IOPS"

	title_format = workbook.add_format({
    'bold': True,
    'text_wrap': False,
    'valign': 'top'
   })
	write_table_to_sheet(pivot_table, writer, table_title, title_format, sheet_name, start_col, start_row)

	start_row += len(table.index)+6
	i += 1
	print(table)

writer.save()




import os
import glob
import sys
import csv
from xlsxwriter.workbook import Workbook


def convert_csv_xlsx(csv_file_name, xlsx_file_name):
	workbook = Workbook(xlsx_file_name, {'strings_to_numbers': True})
	worksheet = workbook.add_worksheet()
	with open(csv_file_name, 'rt', encoding='utf8') as f:
		reader = csv.reader(f)
		for r, row in enumerate(reader):
			for c, col in enumerate(row):
				worksheet.write(r, c, col)
	return (workbook)

#
# args: wb- workbook; sh: sheet; cn: column name
# sr: start row; er: end row
#
def add_line_chart(wb, ws, dict_array, x_axis_name, y_axis_name, start_cell):
# crerate new chart object
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
	ws.insert_chart(start_cell, chart, {'x_scale': 1.5, 'y_scale': 1})



#
# MAIN SCRIPT
# takes argument : time the single test item runs e.g. 120 seconds for normal phase 1 protocol test run
# or 900 seconds for single test run of switch reboot disrupt run
# divide this time by 5 second interval to know what is is the last row so that chart does not take any empty cells
#


x_axis_name = []
y_axis_name = []

last_row = (int(sys.argv[2])/5) + 1
last_row_str = "$" + str(last_row)


for csvfile in glob.glob(os.path.join('.', sys.argv[1])):
	xlsx_filename = csvfile[:-4] + '.xlsx'
	workbook = convert_csv_xlsx(csvfile, xlsx_filename)
	worksheet = workbook.add_worksheet()

#
#Latency chart
#
	x_axis_name.append('Time')
	dictarray = [{'categories': '=Sheet1!$B$2:$B' + last_row_str, 'values': '=Sheet1!$L$2:$L' + last_row_str, 'name': '=Sheet1!$L$1', 
	                 'trendline': {'type': 'polynomial', 'order': 3, 'name': 'Trend line',}, 'line': {'color': 'red'},}]
	y_axis_name.append('Latency')
	chart = add_line_chart(workbook, worksheet, dictarray, x_axis_name, y_axis_name, 'C1')
	y_axis_name.pop()

#
#Throughput chart
#            
	dictarray = [{'categories': '=Sheet1!$B$2:$B' + last_row_str, 'values': '=Sheet1!$H$2:$H' + last_row_str, 'name': '=Sheet1!$I$1', 
	                 'trendline': {'type':  'polynomial', 'order': 3, 'name': 'Trend line',}, 'line': {'color': 'blue'},}]
	y_axis_name.append('Throughput')
	chart = add_line_chart(workbook, worksheet, dictarray, x_axis_name, y_axis_name, 'C15')
	y_axis_name.pop()

#
#IOPS chart
#
	dictarray = [{'categories': '=Sheet1!$B$2:$B' + last_row_str, 'values': '=Sheet1!$D$2:$D' + last_row_str, 'name': '=Sheet1!$E$1', 
	                 'trendline': {'type':  'polynomial', 'order': 3, 'name': 'Trend line',}, 'line': {'color': 'green'},}]
	y_axis_name.append('IOPS')
	chart = add_line_chart(workbook, worksheet, dictarray, x_axis_name, y_axis_name, 'C30')
	y_axis_name.pop()

	workbook.close()

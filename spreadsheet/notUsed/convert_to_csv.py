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
def add_line_chart(wb, dict_array, x_axis_name, y_axis_name):
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
	ws = wb.add_worksheet()
	ws.insert_chart('C1', chart, {'x_scale': 2, 'y_scale': 2})



x_axis_name = []
y_axis_name = []

for csvfile in glob.glob(os.path.join('.', sys.argv[1])):
	xlsx_filename = csvfile[:-4] + '.xlsx'
	workbook = convert_csv_xlsx(csvfile, xlsx_filename)

	dictarray = [{'categories': '=Sheet1!$B$2:$B$121', 'values': '=Sheet1!$L$2:$L$121', 'name': '=Sheet1!$L$1', 
	                 'trendline': {'type': 'polynomial', 'order': 3}, 'line': {'color': 'red'},}, 
	                 {'categories': '=Sheet1!$B$2:$B$121', 'values': '=Sheet1!$I$2:$I$121', 'name': '=Sheet1!$I$1', 
	                 'trendline': {'type':  'polynomial', 'order': 3}, 'y2_axis': 1, 'line': {'color': 'blue'},}]

	x_axis_name.append('Time')
	x_axis_name.append('Time')
	y_axis_name.append('Latency')
	y_axis_name.append('Throughput')
	chart = add_line_chart(workbook, dictarray, x_axis_name, y_axis_name)
	workbook.close()
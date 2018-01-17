import pandas as pd
import numpy as np
import sys

csv_file = sys.argv[1]

pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# reading the date
df1 = pd.read_csv(csv_file, index_col=None)
print(list(df1))
writer = pd.ExcelWriter('output.xlsx')
df1.to_excel(writer, 'Sheet1')
df2 = df1.set_index(' Size')
df3 = df2[[' Q-Depth', ' SD:IOPS', ' SD:MB/S', ' SD:IO Completion Time', ' CPU % Idle Time', ' CPU % Intr Time', ' CPU % Privileged Time', ' CPU % Proc Time', ' CPU % User Time']]
print(df3)
df3.to_excel(writer, 'Sheet2')
table = df3.pivot(columns=' Q-Depth', values=' SD:IOPS')
print(table)
table.to_excel(writer, 'Sheet3')
table = df3.pivot(columns=' Q-Depth', values=' SD:MB/S')
print(table)
table.to_excel(writer, 'Sheet4')
table = df3.pivot(columns=' Q-Depth', values=' SD:IO Completion Time')
print(table)
table.to_excel(writer, 'Sheet5')
writer.save()





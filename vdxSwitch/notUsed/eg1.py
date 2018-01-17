from os import path
import datetime

if path.exists("xyz"):
	print("xyz exists")
else:
	print("file does not exist")
ts='{:%y%m%d%H%M%S}'.format(datetime.datetime.now())
print(ts + ': Waiting for command to start')
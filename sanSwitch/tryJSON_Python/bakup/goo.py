import sys
import pprint
from io import StringIO

_stdout = sys.stdout
print ("After saving sys.stdout")
f = StringIO()
print ("After calling StringIO")
sys.stdout = f
print ("After assigning f to sys.stdout")
sys.stdout = _stdout
print ("After restoring sys.stdout")
print (f.getvalue())
print ("After calling f.getvalue")

x=10
y=20
xy_tup=(x,y)
print(xy_tup[0], xy_tup[1])

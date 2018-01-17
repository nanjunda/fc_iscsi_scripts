import sys
from pprint import pprint

a0=sys.argv[0]
a1=sys.argv[1]
a2=sys.argv[2]
a3=sys.argv[3]
a4=sys.argv[4]
a5=sys.argv[5]
a6=sys.argv[6]

cmd = []
argc=len(sys.argv)
print (argc)
print(a0)
print(a1)
print(a2)
print(a3)
i=4
while (i<argc):
    cmd.append(sys.argv[i])
    i += 1

pprint(cmd)

import sys

#
# convert number to bytes bs (int) to kb (string)


def kb_to_bytes(siz):
    l = len(siz)
    if ("k" in siz):
        b=int(siz[:l-1])*1024
    elif ("m" in siz):
        b = int(siz[:l-1])*1024*1024 
    elif ("b" in siz):
        b = int(siz[:l-1]) 
    return(b)


#
# main script
#
qdepth = sys.argv[1]
buf_size = sys.argv[2]
rd = sys.argv[3]

qstart, qend = qdepth.split('-')
buf_start, buf_end = buf_size.split('-')

q = []
b = []
r = []

m = int(qstart)
n = int(qend)

while (m < 2*n):
    q.append(m)
    m = 2*m


m = kb_to_bytes(buf_start)
n = kb_to_bytes(buf_end)

while (m < 2*n):
    b.append(m)
    m = 2*m

l = len(rd.split('-'))
i = 5 - l
ss = rd
while (i > 0):
    ss = ss + "-XX"
    i -= 1
rd100, rd70, rd50, rd30, rd0 = ss.split('-')
if ("XX" not in rd100):
    r.append(int(rd100))
if ("XX" not in rd70):
    r.append(int(rd70))
if ("XX" not in rd50):
    r.append(int(rd50))
if ("XX" not in rd30):
    r.append(int(rd30))
if ("XX" not in rd0):
    r.append(int(rd0))

print(q)
print(b)
print(r)

import json
import sys

json_file=sys.argv[1]

with open(json_file, "r") as f:
	buf = f.read()
data = json.loads(buf)

read_pct = data["read_pct"]
size_vals = data["io_size"]
qdepth_vals = data["que_depth"]
congestion_pct = data["congestion"]
disruption_type = data["disruption"]

print("read:pct: ", read_pct)
print("size_vals: ", size_vals)
print("qdepth_vals: ", qdepth_vals)
print("congestion: ", congestion_pct)
print("disruption_type: ", disruption_type)



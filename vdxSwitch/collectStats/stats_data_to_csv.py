import sys
import pandas as pd


file_name= "switch_output.txt"
page = []
line = []

with open(file_name, 'r') as f:
	content = f.read().splitlines()
	l = len(content)
	i=0
	num = 1
	while (i < l):
		s = content[i].strip()
		i += 1
		if s[0:3] == "Ten" or s[0:3] == "For":
			line.append(str(num))
			words = s.split(' ')
			for word in words:
				line.append(word)
		if s[-9:] == "line-rate":
			words = s.split(' ')
			for word in words:
				line.append(word)
		if s[0:6] == "Output":
			page.append(line)
#			print(str(line))
			num += 1
			line = []

#	print(len(page))
	for l in page:
#		print(l)
		df = pd.DataFrame(l).T
		df.to_csv(sys.stdout, sep=',')

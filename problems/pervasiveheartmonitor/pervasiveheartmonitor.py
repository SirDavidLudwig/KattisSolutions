import sys
for line in sys.stdin:
	name = ""
	total = 0
	n = 0
	for part in line.split():
		try:
			total += float(part)
			n += 1
		except ValueError:
			name += ' ' + part
	print(total/n, name[1:])

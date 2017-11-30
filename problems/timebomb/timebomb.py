import sys

nums = {
	('***', '* *', '* *', '* *', '***'): 0,
	('  *', '  *', '  *', '  *', '  *'): 1,
	('***', '  *', '***', '*  ', '***'): 2,
	('***', '  *', '***', '  *', '***'): 3,
	('* *', '* *', '***', '  *', '  *'): 4,
	('***', '*  ', '***', '  *', '***'): 5,
	('***', '*  ', '***', '* *', '***'): 6,
	('***', '  *', '  *', '  *', '  *'): 7,
	('***', '* *', '***', '* *', '***'): 8,
	('***', '* *', '***', '  *', '***'): 9
}

values = []

line = sys.stdin.readline()
for i in range(0, len(line), 4):
	values.append([line[i:i+3]])

for line in sys.stdin:
	for i in range(0, len(line), 4):
		values[i//4].append(line[i:i+3])

total = 0
for value in values:
	try:
		total = 10*total + nums[tuple(value)]
	except:
		total = 5
		break

print("BEER!!" if total % 6 == 0 else "BOOM!!")

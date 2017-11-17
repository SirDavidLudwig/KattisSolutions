import sys

values = [
	["xxxxx", "x...x", "x...x", "x...x", "x...x", "x...x", "xxxxx"],
	["....x", "....x", "....x", "....x", "....x", "....x", "....x"],
	["xxxxx", "....x", "....x", "xxxxx", "x....", "x....", "xxxxx"],
	["xxxxx", "....x", "....x", "xxxxx", "....x", "....x", "xxxxx"],
	["x...x", "x...x", "x...x", "xxxxx", "....x", "....x", "....x"],
	["xxxxx", "x....", "x....", "xxxxx", "....x", "....x", "xxxxx"],
	["xxxxx", "x....", "x....", "xxxxx", "x...x", "x...x", "xxxxx"],
	["xxxxx", "....x", "....x", "....x", "....x", "....x", "....x"],
	["xxxxx", "x...x", "x...x", "xxxxx", "x...x", "x...x", "xxxxx"],
	["xxxxx", "x...x", "x...x", "xxxxx", "....x", "....x", "xxxxx"]
]

def display(value):
	chars = [values[int(i)] for i in str(value)]
	for i in range(7):
		print(".".join([rows[i] for rows in chars]))


def asciiToStr(ascii):
	if ascii[0] == "."*5:
		return '+'
	elif ascii[0] == "....x" or ascii[0] == "x...x":
		return str(ascii[0].count('x')**2) # 1, 4
	else:
		if ascii[3] == "....x":
			return '7'
		elif ascii[3] == "x...x":
			return '0'
		elif ascii[4] == "x....":
			return '2'
		elif ascii[4] == "....x":
			if ascii[1] == "....x":
				return '3'
			elif ascii[1] == "x....":
				return '5'
			else:
				return '9'
		elif ascii[1] == "x....":
			return '6'
	return '8'

line = sys.stdin.readline()
chars = [[line[i*6:i*6+5]] for i in range((len(line)+1)//6)]

for line in sys.stdin:
	for i in range((len(line)+1)//6):
		chars[i].append(line[i*6:i*6+5])

display(sum(map(int, "".join([asciiToStr(char) for char in chars]).split('+'))))

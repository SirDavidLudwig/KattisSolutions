from math import ceil

def nextIndex(string, char, start):
	try:
		return string.index(char, start+1)
	except ValueError:
		return -1

for i in range(int(input())):
	line = input().strip('\n')
	j = nextIndex(line, line[0], 0)
	while j != -1 and (line[:j]*ceil(len(line)/j))[:len(line)] != line:
		j = nextIndex(line, line[0], j)
	print(j if j != -1 else len(line))

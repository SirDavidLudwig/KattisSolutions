import sys

n = int(input())
while n != 0:
	maxLen = 0
	lines = []
	for i in range(n):
		lines.append(input())
		maxLen = max(maxLen, len(lines[-1]))
	rotated = [""] * maxLen
	for i in range(maxLen):
		for j in range(len(lines)-1, -1, -1):
			try:
				rotated[i] += lines[j][i]
			except IndexError:
				rotated[i] += ' '
	for line in rotated:
		for char in line.rstrip():
			if char == '-':
				print('|', end='')
			elif char == '|':
				print('-', end='')
			else:
				print(char, end='')
		print()
	n = int(input())
	if n:
		print()

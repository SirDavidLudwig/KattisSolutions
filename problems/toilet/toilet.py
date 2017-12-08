import sys

line = input().strip()
changes = 0
for i in range(1, len(line)):
	changes += line[i] != line[i-1]
print(2*line[1:].count('D') - (line[:2] == "DD") + (line[:2] == "DU"))
print(2*line[1:].count('U') - (line[:2] == "UU") + (line[:2] == "UD"))
print(changes)

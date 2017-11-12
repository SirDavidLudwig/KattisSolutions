
charMap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

line = input().strip().split()
while (line[0] != '0'):
	rot = int(line[0])
	for char in line[1][::-1]:
		print(charMap[(charMap.index(char)+rot)%len(charMap)], end="")
	print()
	line = input().strip().split()

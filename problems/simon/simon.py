import sys

for i in range(int(input())):
	line = input().strip()
	if line.startswith("simon says "):
		print(line[len("simon says "):], end="")
	print()

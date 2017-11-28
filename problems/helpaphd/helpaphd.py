import sys

for i in range(int(input())):
	line = input().strip()
	print("skipped" if line == "P=NP" else sum(map(int, line.split("+"))))

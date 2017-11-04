import sys

pattern = 'PER'
line = sys.stdin.readline().strip()
total = 0
for i in range(len(line)):
	if line[i] != pattern[i%len(pattern)]:
		total += 1
print(total)

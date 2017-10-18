import sys
sys.stdin.readline()
total = 0
for i in sys.stdin.readline().split(" "):
	if (int(i) < 0):
		total += 1
print(total)

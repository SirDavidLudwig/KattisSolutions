import sys

n = int(sys.stdin.readline()) # Discard
line = sys.stdin.readline()

a = lambda x: ('A', 'B', 'C')[x%3]
b = lambda x: ('B', 'A', 'B', 'C')[x%4]
g = lambda x: ('C', 'A', 'B')[x//2%3]

names = ("Adrian", "Bruno", "Goran")
scores = [0, 0, 0]

for i in range(n):
	scores[0] += a(i) == line[i]
	scores[1] += b(i) == line[i]
	scores[2] += g(i) == line[i]

largest = max(scores)
print(largest)
for i in range(3):
	if scores[i] == largest:
		print(names[i])

import sys

largest = 0
member  = 0
for i in range(5):
	score = sum(list(map(int, sys.stdin.readline().split(' '))))
	if score > largest:
		largest = score
		member = i+1
print(member, largest)

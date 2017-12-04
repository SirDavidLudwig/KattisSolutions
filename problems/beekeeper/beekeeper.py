import sys

n = int(input())
search = ["aa", "ee", "ii", "oo", "uu", "yy"]
while n:
	largest = ""
	largestCount = -1
	for i in range(n):
		word = input().strip()
		count = sum((word.count(j) for j in search))
		if count > largestCount:
			largest = word
			largestCount = count
	print(largest)
	n = int(input())

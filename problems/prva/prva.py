import sys

r, c = map(int, input().split())
puzzle = sys.stdin.read()
smallestWord = "z"*21

# Rows
for i in range(r):
	words = sorted([j for j in puzzle[i*(c+1):c+i*(c+1)].split('#') if len(j) >= 2])
	if words and words[0] < smallestWord:
		smallestWord = words[0]

# Columns
for j in range(c):
	words = sorted([i for i in puzzle[j::(c+1)].split('#') if len(i) >= 2])
	if words and words[0] < smallestWord:
		smallestWord = words[0]

print(smallestWord)

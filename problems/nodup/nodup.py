import sys

words = {}
for word in sys.stdin.readline().split():
	if word in words:
		print("no")
		sys.exit(0)
	else:
		words[word] = 1
print("yes")

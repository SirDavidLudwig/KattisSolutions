from math import log2

n, k = map(int, input().split())

if log2(n) <= k:
	print("Your wish is granted!")
else:
	print("You will become a flying monkey!")

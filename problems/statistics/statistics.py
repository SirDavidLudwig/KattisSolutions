import sys

for i, line in enumerate(sys.stdin.readlines()):
	nums = list(map(int, line.split()))[1:]
	mn, mx = min(nums), max(nums)
	print("Case %d: %d %d %d" % (i+1, mn, mx, mx-mn))


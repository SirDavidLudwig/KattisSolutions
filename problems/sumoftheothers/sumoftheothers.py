import sys

for line in sys.stdin:
	nums = tuple(map(int, line.split()))
	total = sum(nums)
	for num in nums:
		if total - num == num:
			print(num)
			break

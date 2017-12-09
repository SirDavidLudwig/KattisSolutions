import sys

branchMap = {}

num = int(input())
for line in sys.stdin:
	if line != "-1":
		nums = tuple(map(int, line.split()))
		for i in nums[1:]:
			branchMap[i] = nums[0]

while num in branchMap:
	print(num, end=" ")
	num = branchMap[num]
print(num)

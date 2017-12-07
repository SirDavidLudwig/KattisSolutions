import sys

def det(nums):
	sNums = sorted(nums)
	diff = sNums[1] - sNums[0]
	for j in range(2, len(nums)):
		if sNums[j] - sNums[j-1] != diff:
			print("non-arithmetic")
			return
	print("arithmetic" if nums == sNums or nums == sNums[::-1] else "permuted arithmetic")


for i in range(int(input())):
	det(list(map(int, input().split()))[1:])

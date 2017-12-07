import sys

n = int(input())
nums = sorted(list(map(int, input().split())))[::-1]
totalDays = 0
for i, num in enumerate(nums):
	totalDays = max(totalDays, num+i+1)
print(totalDays+1)

import sys

n, k = map(int, input().split())

nums = list(range(2, n+1))

crossed = 0
for i in range(len(nums)):
	if nums[i] != -1:
		for j in range(i, len(nums), nums[i]):
			if nums[j] != -1:
				crossed += 1
				if crossed == k:
					print(nums[j])
					sys.exit()
				else:
					nums[j] = -1

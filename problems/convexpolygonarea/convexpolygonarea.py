import sys

for i in range(int(input())):
	nums = tuple(map(int, input().split()))[1:]
	l = sum((nums[k]  *nums[(k+3)%len(nums)] for k in range(0, len(nums), 2)))
	r = sum((nums[k+1]*nums[(k+2)%len(nums)] for k in range(0, len(nums), 2)))
	area = 0.5*(l-r)
	if float.is_integer(area):
		print(int(area))
	else:
		print(area)

import sys

n = int(input())
while n:
	nums = []
	for i in range(n):
		nums = nums + list(map(int, input().split()))
	l = sum((nums[k]  *nums[(k+3)%len(nums)] for k in range(0, len(nums), 2)))
	r = sum((nums[k+1]*nums[(k+2)%len(nums)] for k in range(0, len(nums), 2)))
	area = 0.5*(l-r)
	print("CW" if area < 0 else "CCW", abs(area))
	n = int(input())

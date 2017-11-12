for i in range(int(input())):
	nums = list(map(int, input().strip().split()))[1:]
	avg = sum(nums)/len(nums)
	print("%.3f" % (sum([1 for x in nums if x > avg])/len(nums)*100), end="%\n")

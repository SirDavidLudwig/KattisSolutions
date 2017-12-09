
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def simplifyFraction(n, d):
	if d == 0:
		return None
	cd = gcd(n, d)
	return n/cd, d/cd

_, nums = input(), tuple(map(int, input().split()))

for num in nums[1:]:
	print("%d/%d" % simplifyFraction(nums[0], num))

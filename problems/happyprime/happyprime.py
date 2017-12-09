
def isPrime(n):
	if n == 2 or n == 3:
		return True
	if n & 1 == 0 or n % 3 == 0 or n == 1 or n == 0:
		return False
	i = 5
	w = 2
	while i*i <= n:
		if n % i == 0:
			return False
		i += w
		w = 6 - w
	return True

for i in range(int(input())):
	k, c = map(int, input().split())
	if isPrime(k):
		seen = set()
		m = c
		while m not in seen and m != 1:
			seen.add(m)
			m = sum([int(j)**2 for j in str(m)])
		if m == 1:
			print(k, c, "YES")
			continue
	print(k, c, "NO")

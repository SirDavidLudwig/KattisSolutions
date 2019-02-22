import sys

for i in range(int(input())):
	l = list(map(int, input().split()))

	# Convert from decimal to the proper base by repeated division
	digits = []
	while l[2] != 0:
		digits.append(l[2] % l[1])
		l[2] //= l[1]

	# Calculate sum of squared digits
	s = 0
	for d in digits:
		s += d**2

	# Output
	print(l[0], s)

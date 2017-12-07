import sys

totalMins = totalSecs = 0
for i in range(int(input())):
	m, s = map(int, input().split())
	totalMins += m
	totalSecs += s
print("%0.7f" % (totalSecs/(60*totalMins)) if totalSecs/(60*totalMins) > 1.0 else "measurement error")

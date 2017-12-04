import sys

timeMark = 0
totalDistance = 0
speed = 0

for line in sys.stdin:
	parts = line.split()
	timeParts = list(map(int, parts[0].split(':')))
	time = timeParts[0] + (timeParts[1] + timeParts[2]/60)/60
	if len(parts) == 2:
		totalDistance += (time - timeMark) * speed
		speed = int(parts[1])
		timeMark = time
	else:
		print("%s %.2f km" % (parts[0], totalDistance + (time-timeMark)*speed))


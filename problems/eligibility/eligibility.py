import sys

for i in range(int(sys.stdin.readline())):
	name, studies, birth, courses = sys.stdin.readline().strip().split(" ")
	studies = tuple(map(int, studies.split('/')))
	birth = tuple(map(int, birth.split('/')))
	print(name, end=" ")
	if studies[0] >= 2010 or birth[0] >= 1991:
		print("eligible")
	elif int(courses) > 40:
		print("ineligible")
	else:
		print("coach petitions")

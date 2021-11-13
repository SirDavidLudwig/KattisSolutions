problems = [p.split('-') for p in input().strip().split(';')]

total = 0
for problem in problems:
	if len(problem) == 1:
		total += 1
	else:
		total += int(problem[1]) - int(problem[0]) + 1

print(total)

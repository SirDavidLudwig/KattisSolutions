import sys

voteCount = {}

for line in sys.stdin:
	if line not in voteCount:
		voteCount[line] = 0
	voteCount[line] += 1

candidates = sorted(voteCount.items(), key=lambda item: (item[1], item[0]))[::-1]

if candidates[0][1] == candidates[1][1]:
	print("Runoff!")
else:
	print(candidates[0][0])

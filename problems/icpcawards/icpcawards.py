import sys

winners = set()
for i in range(int(input())):
	parts = input().strip().split()
	if parts[0] not in winners:
		print(" ".join(parts))
		winners.add(parts[0])
	if len(winners) == 12:
		break

import sys

outcomes = {}
for i, num in enumerate((input(), map(int, input().split()))[1]):
	outcomes[num] = False if num in outcomes else i+1

if len(outcomes) == list(outcomes.values()).count(False):
	print("none")
else:
	for i in sorted(outcomes.keys())[::-1]:
		if outcomes[i]:
			print(outcomes[i])
			break

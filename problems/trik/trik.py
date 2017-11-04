import sys

cup = 1

for char in sys.stdin.readline().strip():
	if char == 'A' and cup < 3:
		cup = 1 if cup == 2 else 2
	elif char == 'B' and cup > 1:
		cup = 2 if cup == 3 else 3
	elif char == 'C' and cup != 2:
		cup = 1 if cup == 3 else 3

print(cup)

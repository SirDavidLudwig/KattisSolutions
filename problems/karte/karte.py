import sys

suitMap = ('P', 'K', 'H', 'T')
found = {
	'P': {},
	'K': {},
	'H': {},
	'T': {}
}

line = sys.stdin.readline().strip()

for i in range(0, len(line), 3):
	if line[i+1:i+3] in found[line[i]]:
		print("GRESKA")
		sys.exit(0)
	else:
		found[line[i]][line[i+1:i+3]] = 1

for suit in suitMap:
	print(13 - len(found[suit].keys()), end=" ")
print()

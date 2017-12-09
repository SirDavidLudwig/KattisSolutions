import sys

# Bit masks
BIT_MASK_DIS = 0xfffe
BIT_MASK_EN  = 0x0001

# Generate note map
noteMap = {}
for i, note in enumerate("cdefgab"):
	noteMap[note] = list(range(1, min(4, 8-i))) + list(range(6, 10-i))
	noteMap[note.upper()] = list(range(0, min(4, 8-i))) + list(range(6, 10-i))
noteMap['C'] = [2]

for i in range(int(input())):
	fingerCount = [0]*10
	for note in input().strip():
		for j in range(len(fingerCount)):
			if j not in noteMap[note]:
				fingerCount[j] &= BIT_MASK_DIS
			elif fingerCount[j] & 1 == 0:
				fingerCount[j] = (fingerCount[j]+2) | BIT_MASK_EN
	print(" ".join([str(j >> 1) for j in fingerCount]))

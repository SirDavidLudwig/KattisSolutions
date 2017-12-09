PATTERN = "welcome to code jam"

charMap = {}
for i, char in enumerate(PATTERN[1:]):
	if char not in charMap:
		charMap[char] = []
	charMap[char].append(i)

for i in range(int(input())):
	charCount = [0]*len(PATTERN)
	for char in input().strip():
		if char == PATTERN[0]:
			charCount[0] += 1
		if char in charMap:
			for j in charMap[char]:
				charCount[j+1] += charCount[j]
	print("Case #%d: %04d" % (i+1, int(str(charCount[-1])[-4:])))

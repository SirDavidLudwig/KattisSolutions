string = input().strip()

charCount = {}
for char in string:
	if char not in charCount:
		charCount[char] = 0
	charCount[char] += 1

erased = 0
if len(charCount) > 2:
	for key, value in sorted(charCount.items(), key=lambda v: (v[1], v[0]))[:len(charCount)-2]:
		erased += value
print(erased)

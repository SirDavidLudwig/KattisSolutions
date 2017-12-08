import re
import sys

for line in sys.stdin:
	for word in line.split():
		firstVowel = re.search(r"[aeiouy]", word).start()
		if firstVowel == 0:
			print(word + "yay", end=" ")
		else:
			print(word[firstVowel:] + word[:firstVowel] + "ay", end=" ")
	print()

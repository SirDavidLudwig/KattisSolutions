import re
import sys

wordMap = {
	'0': "zero",
	'1': "one",
	'2': "two",
	'3': "three",
	'4': "four",
	'5': "five",
	'6': "six",
	'7': "seven",
	'8': "eight",
	'9': "nine",
	'10': "ten",
	'11': "eleven",
	'12': "twelve",
	'13': "thirteen",
	'14': "fourteen",
	'15': "fifteen",
	'16': "sixteen",
	'17': "seventeen",
	'18': "eighteen",
	'19': "nineteen",
	'20': "twenty",
	'30': "thirty",
	'40': "forty",
	'50': "fifty",
	'60': "sixty",
	'70': "seventy",
	'80': "eighty",
	'90': "ninety"
}

for line in sys.stdin:
	tokens = re.split("([0-9]+)", line.strip('\n'))
	string = ""
	for i in range(1, len(tokens), 2):
		string += tokens[i-1]
		if tokens[i] in wordMap:
			string += wordMap[tokens[i]]
		else:
			string += "%s-%s" % (wordMap[tokens[i][0] + '0'], wordMap[tokens[i][1]])
	string += tokens[-1]
	print(string[0].upper() + string[1:])

import sys

morseEncode = {
	"A": ".-",
	"H": "....",
	"O": "---",
	"V": "...-",
	"B": "-...",
	"I": "..",
	"P": ".--.",
	"W": ".--",
	"C": "-.-.",
	"J": ".---",
	"Q": "--.-",
	"X": "-..-",
	"D": "-..",
	"K": "-.-",
	"R": ".-.",
	"Y": "-.--",
	"E": ".",
	"L": ".-..",
	"S": "...",
	"Z": "--..",
	"F": "..-.",
	"M": "--",
	"T": "-",
	"G": "--.",
	"N": "-.",
	"U": "..-",
	"_": "..--",
	",": ".-.-",
	".": "---.",
	"?": "----"
}
morseDecode = dict((v, k) for k, v in morseEncode.items())

for line in sys.stdin:
	code = ""
	codeLen = []
	for char in line.strip():
		code += morseEncode[char]
		codeLen.append(len(morseEncode[char]));
	index = 0
	for l in codeLen[::-1]:
		print(morseDecode[code[index:index+l]], end="")
		index += l
	print()

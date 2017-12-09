import sys

hexChars = list("0123456789abcdef")

for line in sys.stdin:
	state = 0
	hexString = ""
	for char in line:
		if state == 0 and char == '0':
			state = 1
		elif state == 1 and char.lower() == 'x':
			state = 2
			hexString += "0" + char
		elif state == 2 and char.lower() in hexChars:
			state = 3
			hexString += char
		elif state == 3:
			if char.lower() in hexChars:
				hexString += char
			else:
				print(hexString, int(hexString, 16))
				hexString = ""
				state = 0

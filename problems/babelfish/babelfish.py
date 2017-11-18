words = {}

parts = input().strip().split()
while parts:
	words[parts[1]] = parts[0]
	parts = input().strip().split()

line = input().strip()
try:
	while line:
		try:
			print(words[line])
		except KeyError:
			print("eh")
		line = input().strip()
except EOFError:
	pass

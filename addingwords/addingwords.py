import sys

env = {}

for line in sys.stdin:
	parts = line.strip().split(" ")
	if parts[0] == "def":
		env[parts[1]] = int(parts[2])
	elif parts[0] == "calc":
		value = 0
		try:
			value = env[parts[1]]
			for i in range(2, len(parts)-1, 2):
				value += env[parts[i+1]] * (1 if parts[i] == '+' else -1)
		except KeyError:
			print(" ".join(parts[1:]), "unknown")
			continue
		result = "unknown"
		for var in env:
			if env[var] == value:
				result = var
		print(" ".join(parts[1:]), result)
	elif parts[0] == "clear":
		env = {}
var = {}
parts = input().strip().split()
while parts[0] != '0':
	if len(parts) > 2 and parts[1] == '=':
		var[parts[0]] = int(parts[2])
	else:
		t = 0
		v = []
		for p in parts:
			if p.isdigit():
				t += int(p)
			elif p != '+':
				if p in var:
					t += var[p]
				else:
					v.append(p)
		if t > 0:
			v = [str(t)] + v
		print(" + ".join(v))

	parts = input().strip().split()

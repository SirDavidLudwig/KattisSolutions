import sys

rows = set()
cols = set()
diag1 = set()
diag2 = set()

t = 0
for i in range(8):
	line = sys.stdin.readline()
	for j in range(8):
		if line[j] == '*':
			t += 1
			if i not in rows and j not in cols and i-j not in diag1 and i+j not in diag2:
				rows.add(i)
				cols.add(j)
				diag1.add(i-j)
				diag2.add(i+j)
			else:
				print("invalid")
				sys.exit()
print("valid" if t == 8 else "invalid")

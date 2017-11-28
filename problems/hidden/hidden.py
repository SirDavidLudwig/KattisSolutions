import sys

s, st = input().strip().split()
indices = {}

for c in s:
	indices[c] = 0

index = -1
valid = True
for c in s:
	try:
		i = st.index(c, indices[c])
		if i > index:
			index = i
			indices[c] = i+1
		else:
			raise ValueError
	except ValueError:
		valid = False
		break

print("PASS" if valid else "FAIL")

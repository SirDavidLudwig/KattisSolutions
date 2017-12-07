
def outer(l):
	for i in range(4*l+1):
		print(('*' if i%12 == 10 else '#') if (i+2)%4 == 0 else '.', end=('\n' if i == 4*l else ''))

def middle(l):
	for i in range(4*l+1):
		print(('*' if i%12 == 9 or i%12 == 11 else '#') if i & 1 else '.', end=('\n' if i == 4*l else ''))

line = input().strip()

outer(len(line))
middle(len(line))
for i in range(4*len(line)+1):
	if (i+2) % 4 == 0:
		print(end=line[(i+2)//4-1])
	else:
		if i & 1 == 0:
			print(end=('*' if (i != 4*len(line) or len(line)%3 != 2) and (i%12 == 8 or (i%12 == 0 and i != 0)) else '#'))
		else:
			print(end='.')
print()
middle(len(line))
outer(len(line))

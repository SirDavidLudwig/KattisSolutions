e, f, c = map(int, input().split())

d = 0
t = e+f
while t >= c:
	d += t//c
	t = t%c+t//c
print(d)

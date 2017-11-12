angle = 360//40
c = list(map(int, input().split()))
while sum(c):
	print(360*3 + angle*((c[0]-c[1])%40 + (c[2]-c[1])%40 + (c[2]-c[3])%40))
	c = list(map(int, input().split()))

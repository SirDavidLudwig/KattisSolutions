
w, l = map(int, input().split())
while w or l:
	x = y = mx = my = 0
	for i in range(int(input())):
		move = input().split()
		if move[0] == 'd':
			my -= int(move[1])
			y = max(0, y-int(move[1]))
		elif move[0] == 'u':
			my += int(move[1])
			y = min(l-1, y+int(move[1]))
		elif move[0] == 'l':
			mx -= int(move[1])
			x = max(0, x-int(move[1]))
		else:
			mx += int(move[1])
			x = min(w-1, x+int(move[1]))
	print("Robot thinks %d %d" % (mx, my))
	print("Actually at %d %d\n" % (x, y))
	w, l = map(int, input().split())

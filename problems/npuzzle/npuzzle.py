import sys

board = sys.stdin.read().replace('\n', '')
t = 0

for i in range(16):
	if board[i] == '.':
		continue
	index = ord(board[i]) - 65
	gr = index // 4
	gc = index % 4
	cr = i // 4
	cc = i % 4
	t += abs(gr - cr) + abs(gc - cc)
print(t)

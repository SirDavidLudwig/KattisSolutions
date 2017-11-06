import sys

board = ['.'*9]*2
for i in range(5):
	board.append('..' + sys.stdin.readline().strip() + '..')
board += ['.'*9]*2

deltas = [(-1, -2), (-1, 2), (-2, -1), (-2, 1)]
t = 0
for i in range(2, 7):
	for j in range(2, 7):
		if board[i][j] == 'k':
			t += 1
			for delta in deltas:
				if board[i+delta[0]][j+delta[1]] == 'k' or board[i-delta[0]][j+delta[1]] == 'k':
					print("invalid")
					sys.exit()
print("valid" if t == 9 else "invalid")

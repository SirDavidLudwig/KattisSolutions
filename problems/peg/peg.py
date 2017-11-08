import sys

board = ["x"*9]*2
for i in range(7):
	if 1 < i < 5:
		board.append("xx" + sys.stdin.readline().strip() + "xx")
	else:
		board.append("x"*4 + sys.stdin.readline().strip() + "x"*4)
board += ["x"*9]*2

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
moves = 0
for i in range(2, 9):
	for j in range(2, 9):
		if board[i][j] == '.':
			for d in delta:
				if board[i-d[0]][j-d[1]] == board[i-2*d[0]][j-2*d[1]] == 'o':
					moves += 1
print(moves)

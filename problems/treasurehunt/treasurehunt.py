import sys

r, c = map(int, input().split())
matrix = [list(input().strip()) for i in range(r)]

moveCount, queue = 0, [(0, 0)]
try:
	while queue:
		p = queue.pop(0)
		if p[0] < 0 or p[1] < 0:
			raise IndexError
		elif matrix[p[0]][p[1]] == '*':
			raise ValueError
		elif matrix[p[0]][p[1]] == 'T':
			print(moveCount)
			break
		elif matrix[p[0]][p[1]] == 'N':
			queue.append((p[0]-1, p[1]))
		elif matrix[p[0]][p[1]] == 'E':
			queue.append((p[0], p[1]+1))
		elif matrix[p[0]][p[1]] == 'S':
			queue.append((p[0]+1, p[1]))
		elif matrix[p[0]][p[1]] == 'W':
			queue.append((p[0], p[1]-1))
		matrix[p[0]][p[1]] = '*'
		moveCount += 1
except IndexError:
	print("Out")
except ValueError:
	print("Lost")

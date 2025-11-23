import sys

GOAL_STATE = (3, '123-')

def neighbors(state):
	i = state[0]
	for d in (1, 2):
		values = list(state[1])
		j = i ^ d
		values[i], values[j] = values[j], values[i]
		yield (j, ''.join(values))

values = ''.join(map(str.strip, sys.stdin.readlines()))
state = (values.index('-'), values)

seen = set([state])
q = [(0, state)]
while len(q) > 0:
	cost, state = q.pop(0)
	if state == GOAL_STATE:
		print(cost)
		break
	for neighbor in neighbors(state):
		if neighbor in seen:
			continue
		seen.add(neighbor)
		q.append((cost + 1, neighbor))
else:
	raise Exception("Unsolvable")

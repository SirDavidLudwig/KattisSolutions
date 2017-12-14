x = int(input())
d = total = 0
queue = list(input().strip())
while queue and -x <= d <= x:
	if d > 0:
		if len(queue) > 1 and queue[1] == 'W':
			result = queue.pop(1)
		else:
			result = queue.pop(0)
	else:
		if len(queue) > 1 and queue[1] == 'M':
			result = queue.pop(1)
		else:
			result = queue.pop(0)
	d += 1 if result == 'M' else -1
	total += 1
print(total - (1 if abs(d) > x else 0))

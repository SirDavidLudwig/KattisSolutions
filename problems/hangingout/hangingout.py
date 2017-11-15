import sys

l, n, total, denied = map(int, input().split()+[0, 0])
for i in range(n):
	event, value = input().strip().split()
	if event == 'enter':
		if int(value) + total > l:
			denied += 1
		else:
			total += int(value)
	elif event == 'leave':
		total -= int(value)
print(denied)


n, t = map(int, input().split())
tasks = tuple(map(int, input().split()))
tot = 0
i = 0
while tot <= t and i < len(tasks):
	tot += tasks[i]
	i += 1

print(i if tot <= t else i-1)

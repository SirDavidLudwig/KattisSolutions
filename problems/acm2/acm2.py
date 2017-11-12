n, p = map(int, input().split())
times = list(map(int, input().split()))

start = times.pop(p)
times.sort()
times = [start] + times

totalTime = compTime = i = 0

while i < len(times) and times[i] + compTime <= 300:
	totalTime += compTime + times[i]
	compTime += times[i]
	i += 1

print(i, totalTime)

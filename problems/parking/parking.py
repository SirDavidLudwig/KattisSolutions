import sys

fee = [0] + list(map(int, sys.stdin.readline().split()))

trucks = [[False]*101, [False]*101, [False]*101]
begin = 999999
end = -1
for i in range(3):
	start, stop = map(int, sys.stdin.readline().split())
	for j in range(start+1, stop+1):
		trucks[i][j] = True
		begin = min(begin, start+1)
		end = max(end, stop+1)

total = 0
for i in range(begin, end):
	s = sum([trucks[j][i] for j in range(3)])
	total += s*fee[s]

print(total)

import sys

line = sys.stdin.readline()

score = min(line.count('C'), line.count('T'), line.count('G'))*7
print(score + line.count('C')**2 + line.count('T')**2 + line.count('G')**2)

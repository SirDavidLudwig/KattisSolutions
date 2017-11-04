import sys

values = sorted(list(map(int, sys.stdin.readline().split(' '))))

print(values[0] * values[2])

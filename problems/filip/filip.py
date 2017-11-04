import sys

print(max(*(int(i[::-1]) for i in sys.stdin.readline().split(' '))))

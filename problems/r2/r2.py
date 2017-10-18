import sys
r1, s = (int(i) for i in sys.stdin.readline().strip().split(" "))
print(s*2-r1)

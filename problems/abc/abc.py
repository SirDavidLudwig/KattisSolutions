import sys
v = sorted([int(i) for i in sys.stdin.readline().strip().split(' ')])
print(" ".join([str(v[ord(i)-65]) for i in sys.stdin.readline().strip()]))
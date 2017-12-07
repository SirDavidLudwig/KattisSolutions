from math import cos, floor, radians
import sys

h, v = map(int, input().split())
print("safe" if 0 <= v <= 180 else floor(abs(h/cos(radians(270-v)))))

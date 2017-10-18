#!/usr/bin/python3
from math import sqrt
import sys

value = int(sys.stdin.readline().strip())
result = sqrt(value)*4

if result == int(result):
	print(int(result))
else:
	print(result)
from datetime import datetime
import sys

parts = tuple(map(int, sys.stdin.readline().split(" ")))

print(datetime(2009, parts[1], parts[0]).strftime("%A"))

import sys

a = sum(map(int, sys.stdin.readline().split()))
b = sum(map(int, sys.stdin.readline().split()))

if a > b:
	print("Gunnar")
elif a < b:
	print("Emma")
else:
	print("Tie")

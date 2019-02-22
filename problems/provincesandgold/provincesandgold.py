import sys

g, s, c = map(int, input().split())

buyingPower = g*3 + s*2 + c

if buyingPower >= 8:
	print("Province or ", end="")
elif buyingPower >= 5:
	print("Duchy or ", end="")
elif buyingPower >= 2:
	print("Estate or ", end="")

if buyingPower >= 6:
	print("Gold")
elif buyingPower >= 3:
	print("Silver")
else:
	print("Copper")

import sys

# Formula: x + yn = n => n = x/(1-y)
# y != 1, so impossible in this case, unless x is already at 0

x, y = map(int, input().split())
if y == 1:
	if x == 0:
		print("ALL GOOD")
	else:
		print("IMPOSSIBLE")
elif x == 0:
	print("0.00000")
else:
	n = x/(1-y)
	print(int(n) if float(n).is_integer() else ("{:.6f}".format(n)))

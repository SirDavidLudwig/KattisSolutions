import sys

sweet, sour = map(int, input().split())

while sweet or sour:
	if sweet + sour == 13:
		print("Never speak again.")
	elif sweet > sour:
		print("To the convention.")
	elif sweet < sour:
		print("Left beehind.")
	else:
		print("Undecided.")
	sweet, sour = map(int, input().split())

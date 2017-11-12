t = int(input())

for i in range(t):
	input()
	input()
	if max(map(int, input().split())) >= max(map(int, input().split())):
		print("Godzilla")
	else:
		print("MechaGodzilla")

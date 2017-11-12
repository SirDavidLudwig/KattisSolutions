for i in range(int(input())):
	input()
	total, n = 0, int(input())
	for j in range(n):
		total += int(input())
	print("NO" if total % n else "YES");

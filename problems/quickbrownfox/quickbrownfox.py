a = set([c for c in 'abcdefghijklmnopqrstuvwxyz'])
for i in range(int(input())):
	n = set(c for c in input().strip().lower() if c.isalpha())
	if list(a - n):
		print("missing", "".join(sorted(list(a-n))))
	else:
		print("pangram")

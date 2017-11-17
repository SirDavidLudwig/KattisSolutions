for i in range(int(input())):
	table = {}
	for j in range(int(input())):
		name, classLevel, _ = input().strip().split()
		priority = 0x55555
		for cl in classLevel.split('-'):
			priority = (priority >> 2) | (min(ord(cl[0])-ord('l'), 2) << 18)
		try:
			table[priority].append(name[:-1])
		except KeyError:
			table[priority] = [name[:-1]]
	for value in sorted(table.keys())[::-1]:
		for name in sorted(table[value]):
			print(name)
	print("="*30)

if int(input()) & 1:
	value = input().strip().translate({48: 49, 49: 48})
else:
	value = input().strip()
print("Deletion", ("succeeded" if input().strip() == value else "failed"))

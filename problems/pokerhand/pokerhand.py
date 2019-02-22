values = {}
for card in input().strip().split():
	if card[0] not in values:
		values[card[0]] = 1
	else:
		values[card[0]] += 1
print(max(values.values()))

notes = {n: "" for n in "abcdefgABCDEFG"[::-1]}
staffs = {n: '-' if n in "FDBgea" else ' ' for n in notes}

input()
for note in input().strip().split():
	note, length = note[0], int(note[1:] or '1')
	notes[note] += '*'*length + staffs[note]
	for n in notes:
		if n == note:
			continue
		notes[n] += staffs[n]*(length+1)

for n in notes:
	print(f"{n}: {notes[n][:-1]}")

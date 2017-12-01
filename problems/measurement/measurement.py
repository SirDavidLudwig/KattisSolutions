import sys

nameConversion = {
	"thou":   "th",
	"inch":    "in",
	"foot":    "ft",
	"yard":    "yd",
	"chain":   "ch",
	"furlong": "fur",
	"mile":    "mi",
	"league":  "lea"
}

units = {
	"th":  None,
	"in":  1000,
	"ft":  12,
	"yd":  3,
	"ch":  22,
	"fur": 10,
	"mi":  8,
	"lea": 3
}

unitOrder = ['th', 'in', 'ft', 'yd', 'ch', 'fur', 'mi', 'lea']

line  = input().strip().split()
value = int(line[0])
unitsFrom = line[1]  if line[1]  in units else nameConversion[line[1]]
unitsTo   = line[-1] if line[-1] in units else nameConversion[line[-1]]

orderFrom = unitOrder.index(unitsFrom)
orderTo   = unitOrder.index(unitsTo)

if orderFrom > orderTo:
	for unit in unitOrder[orderFrom:orderTo:-1]:
		value *= units[unit]
else:
	for unit in unitOrder[orderFrom+1:orderTo+1]:
		value /= units[unit]
print(value)

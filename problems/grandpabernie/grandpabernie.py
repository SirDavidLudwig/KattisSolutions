
trips = {}

for i in range(int(input())):
	country, year = input().split()
	if country not in trips:
		trips[country] = []
	trips[country].append(int(year))

for country in trips:
	trips[country].sort()

for i in range(int(input())):
	country, k = input().split()
	print(trips[country][int(k)-1])

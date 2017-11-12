for i in range(int(input())):
	sounds = input().strip().split()
	line = input().strip()
	while line != "what does the fox say?":
		sounds = list(filter((line.split(" ")[-1]).__ne__, sounds))
		line = input().strip()
	print(" ".join(sounds))

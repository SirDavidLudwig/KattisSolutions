import sys


def main():
	line = sys.stdin.readline()
	left = line[0:len(line)//2]
	right = line[len(line)//2:]
	result = ""
	t1 = t2 = 0
	for i in range(len(left)):
		t1 += ord(left[i])  - 65
		t2 += ord(right[i]) - 65
	for i in range(len(left)):
		b = (ord(right[i])-65+t2)
		result += chr(65+(ord(left[i])-65+t1+b)%26)
	print(result)
	return 0


if __name__ == "__main__":
	sys.exit(main())

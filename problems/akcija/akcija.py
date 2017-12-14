books = sorted([int(input()) for i in range(int(input()))])[::-1]
print(sum((v for i, v in enumerate(books) if (i+1) % 3)))

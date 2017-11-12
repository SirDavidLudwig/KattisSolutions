h, w, kh, kw = map(int, input().split())

image = []
kernel = []
for i in range(h):
	image.append(list(map(int, input().split())))

for i in range(kh):
	kernel = [(list(map(int, input().split()))[::-1])] + kernel

for i in range(h - kh + 1):
	for j in range(w - kw + 1):
		t = 0
		for k in range(kh):
			for l in range(kw):
				t += kernel[k][l]*image[i+k][j+l]
		print(t, end=' ')
	print()


def run(maxWidth):
	largestWidth = currentWidth = prevHeight = currentHeight = 0
	w, h = map(int, input().split())
	while w != -1:
		if w + currentWidth > maxWidth:
			largestWidth = max(currentWidth, largestWidth)
			prevHeight += currentHeight
			currentWidth = w
			currentHeight = h
		else:
			currentWidth += w
			currentHeight = max(currentHeight, h)
		w, h = map(int, input().split())
	print(max(largestWidth, currentWidth), 'x', currentHeight + prevHeight)

m = int(input())
while m:
	run(m)
	m = int(input())

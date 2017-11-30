from math import sqrt
import sys

class Rect:
	def __init__(self, x1, y1, x2, y2):
		self.__x1, self.__y1, self.__x2, self.__y2 = x1, y1, x2, y2
	def hit(self, x, y):
		return self.__x1 <= x <= self.__x2 and self.__y1 <= y <= self.__y2

class Circle:
	def __init__(self, x, y, radius):
		self.__x, self.__y, self.__radius = x, y, radius
	def hit(self, x, y):
		return sqrt((x-self.__x)**2 + (y-self.__y)**2) <= self.__radius

targets = []

for i in range(int(input())):
	line = input().strip().split()
	values = map(int, line[1:])
	if line[0] == "circle":
		targets.append(Circle(*values))
	else:
		targets.append(Rect(*values))

for i in range(int(input())):
	hit = 0
	x, y = map(int, input().split())
	for target in targets:
		hit += target.hit(x, y)
	print(hit)

import numpy
from matplotlib import pyplot
import random
import math

RADIUS = 1

def monte_carlo(n):
	X_circle, Y_circle, X_square, Y_square = numpy.empty(1), numpy.empty(1), numpy.empty(1), numpy.empty(1)

	circle_area = 0
	total_area = 0

	for i in range(n):
		x = random.random()
		y = random.random()
		r = math.sqrt((x**2) + (y**2))
		total_area += 1
		if r > RADIUS:
			X_square = numpy.append(X_square, x)
			Y_square = numpy.append(Y_square, y)
		else:
			X_circle = numpy.append(X_circle, x)
			Y_circle = numpy.append(Y_circle, y)
			circle_area += 1

	ratio = circle_area / total_area

	print(f'Total points:          {total_area}')
	print(f'Points inside circle:  {circle_area}')
	print(f'Points outside circle: {total_area - circle_area}')
	print(f'Ratio circle:square :  {ratio}')
	print(f'Pi:                    {ratio * 4}')

	pyplot.scatter(X_circle, Y_circle, c="red")
	pyplot.scatter(X_square, Y_square, c="black")
	pyplot.axis([0,1,0,1])
	pyplot.show()

monte_carlo(100000)

import random
import math
import numpy
from matplotlib import pyplot
from collections import Counter

class Element:
	def __init__(self, val=0):
		self.val = val

class Stream:
	def __init__(self):
		self.element = Element()
		self.index = 1
		self.__eof = random.randint(1,1000)

	def next(self):
		self.element = Element(self.index + 1)
		self.index += 1

	def get_size(self):
		return self.__eof

	def get_random(self):
		stored_element = self.element
		n = 1
		while n < self.__eof:
			r = random.random()
			if ((1 / n) > r):
				stored_element = self.element
			self.next()
			n += 1

			
		return stored_element.val


def validate_randomness(tests):
	data = []

	for i in range(tests):
		stream = Stream()
		size = stream.get_size()
		probability = round(stream.get_random() / size, 2)
		data.append(probability)

	data_counter = Counter(data)
	data_counter_sorted = sorted(data_counter.items())

	print(data_counter_sorted)
	probabilities = [i[0] for i in data_counter_sorted] 
	frequency = [i[1] for i in data_counter_sorted] 
	width = 0.001

	pyplot.bar(probabilities, frequency, width=width)
	pyplot.show()

validate_randomness(100000)
# print(Stream().get_random())

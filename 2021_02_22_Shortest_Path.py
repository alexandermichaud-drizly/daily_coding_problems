import numpy as np

class Matrix:

	def __init__(self, matrix):
		self.matrix = matrix
		self.log = {}

	def find_shortest_path(self,start,finish,last=None):
		print(start)
		if last is None:
			self.log[start] = 0
			self.log[finish] = None
		else:
			steps = self.log[last] + 1
			self.log[start] = steps if start not in self.log or self.log[start] == None else min(steps, self.log[start])
		
		look_up, look_right, look_down, look_left =\
			(start[0],     start[1] + 1), \
			(start[0] + 1, start[1]), \
			(start[0],     start[1] - 1), \
			(start[0] - 1, start[1]) 

		look_around = [look_up, look_right, look_down, look_left]
		for move in look_around:
			if move not in self.log and move[0] > -1 and move[1] > -1 and move[0] < self.matrix.shape[0] and move[1] < self.matrix.shape[1]:
				if self.matrix[move[0],move[1]]:
					self.log[move] = -1
				else:
					self.find_shortest_path(move,finish,start)
				print(self.log)
		return self.log[finish]
			

test_1 = np.array([\
	[0,0,0,0],\
	[1,1,0,1],\
	[0,0,0,0],\
	[0,0,0,0]])

matrix = Matrix(test_1)
print(matrix.find_shortest_path((0,0), (3,0)))

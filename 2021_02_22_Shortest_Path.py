import numpy as np

class Matrix:

	def __init__(self, matrix):
		self.matrix = matrix

	def find_shortest_path(self,start,finish, visited={}):
		print(start)
		if start == finish:
			return 0

		visited[start] = True
		
		look_up, look_right, look_down, look_left =\
			(start[0],     start[1] + 1), \
			(start[0] + 1, start[1]), \
			(start[0],     start[1] - 1), \
			(start[0] - 1, start[1]) 

		look_around = [look_up, look_right, look_down, look_left]
		min_path = None
		for move in look_around:
			if move not in visited and move[0] > -1 and move[1] > -1 and move[0] < self.matrix.shape[0] and move[1] < self.matrix.shape[1]:
				if self.matrix[move[0],move[1]]:
					visited[move] = True
				else:
					path = self.find_shortest_path(move,finish,visited.copy())
					if path is None:
						pass
					elif min_path is None:
						min_path = path + 1
					else: 
						min_path = min(min_path, path + 1)
		return min_path
			

test_1 = np.array([\
	[0,0,0,0],\
	[1,1,0,1],\
	[0,0,0,0],\
	[0,0,0,0]])

test_2 = np.array([\
	[0,0,0,0,0],\
	[1,1,1,1,0],\
	[0,0,0,1,0],\
	[1,1,0,1,0],\
	[0,0,0,0,0],\
	[0,1,0,1,0],\
	[0,1,0,0,0]])


matrix = Matrix(test_1)
print(matrix.find_shortest_path((0,0), (3,0)))
matrix = Matrix(test_2)
print(matrix.find_shortest_path((0,0), (6,0)))


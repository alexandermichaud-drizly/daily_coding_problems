import numpy

class Board():
	def __init__(self):
		self.__squares = numpy.zeros((8,8))

	def show(self):
		print(self.__squares)

	def place_eight_queens(self):
		self.__eight_queens_helper()
		print(self.__squares)

	def __queen_helper(self, x, y, place=1):
		self.__squares[x,y] = place

	def __eight_queens_helper(self, row=0, column=0):
		valid_placement = False 
		working_column = column

		while working_column < 8 and not valid_placement:
			self.__queen_helper(row, working_column)
			self.show()
			valid_placement = not self.__collisions_exist(row, working_column)
			if valid_placement and row == 7:
				return True
			elif valid_placement and row < 7:
				valid_placement = self.__eight_queens_helper(row=row+1)
			
			if not valid_placement:
				self.__queen_helper(row, working_column, place=0)
			working_column += 1

		return valid_placement
		
	def __collisions_exist(self, x, y):
		print(f'x: {x}; y: {y}')
		# Check Verticals
		column = self.__squares[:,y]
		for i, square in enumerate(column):
			if square == 1 and i is not x:
				# print("failed vertical")
				return True

		# Check Diagonal
		diag = self.__squares.diagonal(y - x)
		axis = x if y > x else y
		for i, square in enumerate(diag):
			if square == 1 and i is not axis:
				# print(f'failed diagonal: {i} in {diag}')
				return True

		# Check Antidiagonal
		flipped_board = numpy.fliplr(self.__squares).copy()
		squares_reversed = range(7,-1,-1)
		antidiag = flipped_board.diagonal(squares_reversed[y] - x)
		axis = max(x,y)
		for i, square in enumerate(antidiag):
			if square == 1 and i is not squares_reversed[axis]:
				# print(f'failed antidiagonal: {i} in {antidiag}')
				return True
		
		# No Collisions
		return False

board = Board()
board.place_eight_queens()

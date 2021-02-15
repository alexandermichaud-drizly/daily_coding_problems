import numpy

class Board():
	def __init__(self):
		self.__squares = numpy.zeros((8,8))

	def show(self):
		print(self.__squares)

	def place_eight_queens(self, starting_column=0):
		self.__queen_helper(0, starting_column)
		self.__eight_queens_helper()
		print(self.__squares)

	def __queen_helper(self, x, y, place=1):
		print(f'x: {x}, y: {y}')
		self.__squares[x,y] = place

	def __eight_queens_helper(self, row=1, column=0):
		valid_placement = False 

		self.__queen_helper(row, column)
		valid_placement = not self.__collisions_exist(row, column)

		if not valid_placement and column < 7:
			self.__queen_helper(row,column,place=0)
			valid_placement = self.__eight_queens_helper(row, column=column+1)

		return self.__eight_queens_helper(row=row+1) if valid_placement and row < 7 else valid_placement

	def __collisions_exist(self, x, y):
		# Check Verticals
		column = self.__squares[:,y]
		for i, square in enumerate(column):
			if square == 1 and i is not x:
				return True

		# Check Diagonal
		diag = self.__squares.diagonal(y - x)
		for i, square in enumerate(diag):
			if square == 1 and i is not y:
				return True

		# Check Antidiagonal
		flipped_board = numpy.fliplr(self.__squares).copy()
		columns_reversed = range(7,-1,-1)
		antidiag = flipped_board.diagonal(columns_reversed[y] - x) 
		for i, square in enumerate(antidiag):
			if square == 1 and i is not columns_reversed[y]:
				return True
		
		# No Collisions
		return False

board = Board()
board.place_eight_queens()

import numpy

class Board():
	def __init__(self):
		self.__squares = numpy.zeros((8,8))

	def show(self):
		print(self.__squares)
	
	def clear(self):
		self.__squares = numpy.zeros((8,8))

	def count_eight_queens(self):
		return self.__eight_queens_helper()

	def __queen_helper(self, x, y, place=1):
		self.__squares[x,y] = place

	def __eight_queens_helper(self, row=0):
		valid_placement = False 
		count = 0

		for working_column in range(8):
			print(f'Checking row {row} column {working_column}')
			self.__queen_helper(row, working_column)
			if self.__no_collisions(row, working_column):
				if row == 7:
					count += 1
				elif row < 7:
					count += self.__eight_queens_helper(row+1)
			self.__queen_helper(row, working_column, place=0)
			
		return count 
		
	def __no_collisions(self, x, y):
		# Check Verticals
		column = self.__squares[:,y]
		column = numpy.delete(column, x)
		for square in column:
			if square == 1:
				return False

		# Check Diagonal
		diag = self.__squares.diagonal(y - x)
		delete = x if y > x else y
		diag = numpy.delete(diag, delete)
		for square in diag:
			if square == 1:
				return False

		# Check Antidiagonal
		flipped_board = numpy.fliplr(self.__squares).copy()
		squares_reversed = range(7,-1,-1)
		y_reversed = squares_reversed[y]
		anti_diag = flipped_board.diagonal(y_reversed - x)
		delete = x if y_reversed > x else y_reversed
		anti_diag = numpy.delete(anti_diag, delete)
		for square in anti_diag:
			if square == 1:
				return False
		
		# No Collisions
		return True

board = Board()
print(board.count_eight_queens())


import numpy

class Board():
	def __init__(self):
		self.__squares = numpy.zeros((8,8))
		self.__search_steps = 0

	def show(self):
		print(self.__squares)
	
	def clear(self):
		self.__squares = numpy.zeros((8,8))
		self.__search_steps = 0

	def place_eight_queens(self, column_start=0):
		self.__eight_queens_helper(0, column_start)
		self.show()
		print(f'Search Steps: {self.__search_steps}')

	def __queen_helper(self, x, y, place=1):
		self.__squares[x,y] = place

	def __eight_queens_helper(self, row=0, column=0):
		self.__search_steps += 1
		valid_placement = False 
		working_column = column

		while working_column < 8 and not valid_placement:
			self.__queen_helper(row, working_column)
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
		# Check Verticals
		column = self.__squares[:,y]
		column = numpy.delete(column, x)
		for square in column:
			if square == 1:
				return True

		# Check Diagonal
		diag = self.__squares.diagonal(y - x)
		delete = x if y > x else y
		diag = numpy.delete(diag, delete)
		for square in diag:
			if square == 1:
				return True

		# Check Antidiagonal
		flipped_board = numpy.fliplr(self.__squares).copy()
		squares_reversed = range(7,-1,-1)
		y_reversed = squares_reversed[y]
		anti_diag = flipped_board.diagonal(y_reversed - x)
		delete = x if y_reversed > x else y_reversed
		anti_diag = numpy.delete(anti_diag, delete)
		for square in anti_diag:
			if square == 1:
				return True
		
		# No Collisions
		return False

board = Board()

for i in range(8):
	board.place_eight_queens(i) 
	board.clear()


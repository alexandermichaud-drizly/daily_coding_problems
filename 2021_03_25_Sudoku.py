import numpy as np

test_puzzle = np.array([\
    [None,None,   1, None,None,None, None,   7,None],\
    [None,None,None, None,None,   5, None,None,None],\
    [None,   9,None, None,   7,None,    2,None,   1],\
    \
    [None,   7,None,    3,None,None, None,None,None],\
    [None,None,   5, None,   6,None, None,None,None],\
    [None,None,   4, None,None,None,    3,None,None],\
    \
    [   4,None,None, None,None,None, None,   9,None],\
    [None,   3,None, None,   5,None, None,None,   6],\
    [None,None,   7, None,None,None, None,   4,None]])

class Sudoku:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def solve(self):
        self.puzzle = self.recursive_solve(self.puzzle, 0, 0)

    def recursive_solve(self, puzzle, row, col):
        if puzzle[row,col] is None:
            for n in range(1,10):
                if not self.invalid((row,col), puzzle, n):
                    puzzle[row,col] = n
                    if row == 8 and col == 8:
                        return puzzle
                    elif col == 8:
                        return self.recursive_solve(puzzle, row + 1, 0)
                    else:
                        return self.recursive_solve(puzzle, row, col + 1)
            return None
        else:
            if row == 8 and col == 8:
                return puzzle
            elif col == 8:
                return self.recursive_solve(puzzle, row + 1, 0)
            else:
                return self.recursive_solve(puzzle, row, col + 1)


    def invalid(self, pos, grid, n):
        row= grid[:,pos[1]]
        col = grid[pos[0],:]

        if n in row or n in col:
            return True

        square = (pos[0] // 3, pos[1] // 3)

        for i in range(3):
            for j in range(3):
                if grid[(square[0] * 3) + i,(square[1] * 3) + j] == n:
                    return True

        return False
        
if __name__ == "__main__":
    sudoku = Sudoku(test_puzzle)
    sudoku.solve()        
    print(sudoku.puzzle)


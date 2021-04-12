import numpy as np

test_arr = np.array([[1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]])

class Spiral:
    def __init__(self,matrix):
        self.matrix = matrix

    def unravel(self):
        shape = np.shape(self.matrix)
        right_bound = shape[1]
        lower_bound = shape[0]
        left_bound  = -1
        upper_bound = 0

        pos = [0,0]

        spiral = True
        while spiral:
            spiral = False

            if pos[1] < right_bound:
                while pos[1] < right_bound:
                    print(self.matrix[pos[0],pos[1]])
                    pos[1] += 1
                right_bound -= 1
                spiral = True

            if pos[0] < lower_bound:
                while pos[0] < lower_bound:
                    print(pos)
                    print(self.matrix[pos[0],pos[1]])
                    pos[1] += 1
                right_bound -= 1
                spiral = True
          
            if pos[1] > left_bound:
                while pos[1] > left_bound:
                    print(self.matrix[pos[0],pos[1]])
                    pos[1] -= 1
                left_bound += 1
                spiral = True

            if pos[0] > upper_bound:
                while pos[0] > upper_bound:
                    print(self.matrix[pos[0],pos[1]])
                    pos[0] -= 1
                upper_bound += 1
                spiral = True

if __name__ == "__main__":
    spiral = Spiral(test_arr)
    spiral.unravel()

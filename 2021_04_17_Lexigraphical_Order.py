import numpy as np

def columns_to_remove(matrix: np.matrix) -> int:
    d = 0
    c = matrix.shape[1]
    for i in range(c):
        column = matrix[:,i]
        j = 0
        k = 1
        while k < len(column):
            if column[j] > column[k]:
                d += 1
                break
            j += 1
            k += 1
    return d

if __name__ == "__main__":
    test = np.matrix([['a','b','c'],['b','a','z'],['c','c','w']])
    print(columns_to_remove(test))
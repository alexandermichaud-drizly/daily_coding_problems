import numpy as np
from collections import namedtuple
from functools import reduce

House = namedtuple('House', ['address', 'color'])

def build_matrix(n,k):
    return np.matrix(np.random.randint(1,25,size=(n,k)))

def search_helper(matrix, n=0, k=0):
    if matrix.shape[0] == n:
        return [] 
    else: 
        minimum = -1
        chepeast_row = []
        for i in range(matrix.shape[1]):
            if i is not k:
                best_row = search_helper(matrix, n + 1, i)
                sum = 0
                for house in best_row:
                    sum += matrix[house.address, house.color]
                cost = matrix[n,i] + sum
                if minimum < 0 or cost < minimum:
                    minimum = cost 
                    cheapest_row = [House(n,i)] + best_row
        return cheapest_row

def minimum_cost(n,k):
    matrix = build_matrix(n,k)
    print(matrix)
    return search_helper(matrix)

print(minimum_cost(5,5))
print(minimum_cost(8,5))
print(minimum_cost(5,5))
print(minimum_cost(1,5))
print(minimum_cost(2,2))

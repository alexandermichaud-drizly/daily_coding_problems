def matrix_search(n,m,pos=(0,0)):
    if pos == (n - 1, m - 1):
        return 1
    
    count = 0
    if pos[0] < n - 1:
        count += matrix_search(n,m,(pos[0] + 1, pos[1]))
    if pos[1] < m - 1:
        count += matrix_search(n,m,(pos[0], pos[1] + 1))
    return count


assert matrix_search(2,2) == 2
assert matrix_search(5,5) == 70
print(matrix_search(4,4))
print(matrix_search(7,3))

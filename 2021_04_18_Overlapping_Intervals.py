test = [(1, 3), (5, 10), (4, 8), (9, 12)]

def eliminate_overlap(arr):
    arr = sorted(arr, key=lambda x: x[0])
    i = 0
    while i < len(arr) - 1:
        m,n = arr[i],arr[i + 1]
        if m[1] > n[0]:
            start = min(m[0],n[0])
            fin = max(m[1],n[1])
            interval = (start,fin)
            arr = arr[:i] + [interval] + arr[(i+2):] if len(arr) > i + 2 else arr[:i] + [interval]
        else:
            i += 1
    
    return arr


print(eliminate_overlap(test))

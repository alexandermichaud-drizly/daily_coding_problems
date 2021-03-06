def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def sort_rgb(arr):
    i = 0
    j = 1

    while i < len(arr) - 1:
        left = arr[i]
        right = arr[j]

        if right == 'R':
            swap(arr,i,j)
            i += 1
        else:
            if left == 'B':
                swap(arr,i,j)
            j += 1

        if j == len(arr):
            i += 1
            j = i + 1

    return arr

test_arr = ['G','B','R','R','B','R','G']

print(sort_rgb(test_arr))

test_arr = [1,5,2,2,3,8,4,11,5]

def find_sum(arr, k):
    left = 0
    right = 0
    temp = []
    s = 0

    while left < len(arr) and right < len(arr):
        n = arr[right]
        temp.append(n)
        s += n
        if s == k:
            return temp
         
        while s > k:
            left += 1
            p = temp.pop(0)
            s -= p

            if s == k:
                return temp

        right += 1

print(find_sum(test_arr, 25))

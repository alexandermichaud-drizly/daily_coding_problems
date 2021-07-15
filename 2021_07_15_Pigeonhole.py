def find_duplicate(lst: list) -> int:
    for i in lst:
        j = abs(i)
        if lst[j] < 0:
            return j
        lst[j] *= -1


if __name__ == "__main__":
    assert find_duplicate([3,4,1,3,5,4]) == 3
    assert find_duplicate([2,4,7,8,5,6,1,3,9,8]) == 8
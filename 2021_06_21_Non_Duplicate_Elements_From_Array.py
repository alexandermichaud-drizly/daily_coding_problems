def non_duplicates(l: list) -> list:
    i = 2
    while i < len(l):
        if l[0] == l[1]:
            l.pop(1)
            l.pop(0)
            i = 2
        elif l[0] == l[i]:
            l.pop(i)
            l.pop(0)
            i = 2
        elif l[1] == l[i]:
            l.pop(i)
            l.pop(1)
            i = 2
        else:
            i += 1
    return l[:2]

if __name__ == "__main__":
    print(non_duplicates([2, 4, 6, 8, 10, 2, 6, 10]))
    print(non_duplicates([1, 2, 3, 4, 5, 6, 1, 2, 3, 5]))
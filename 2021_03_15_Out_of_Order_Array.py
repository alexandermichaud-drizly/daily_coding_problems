def get_inversions(l):
    if len(l) == 1:
        return (0, l)

    first = l[:len(l)//2]
    last  = l[len(l)//2:]

    top    = get_inversions(first) 
    bottom = get_inversions(last)
    count_top, count_bottom, top_list, bottom_list = top[0], bottom[0], top[1], bottom[1]

    count = count_top + count_bottom
    merged = []
    while len(top_list) > 0 or len(bottom_list) > 0:
        if len(top_list) == 0:
            merged += bottom_list
            bottom_list = []
        elif len(bottom_list) == 0:
            merged += top_list
            top_list = []
        elif top_list[0] < bottom_list[0]:
            merged.append(top_list.pop(0))
        else:
            count += len(top_list)
            merged.append(bottom_list.pop(0))


    return (count, merged)

print(get_inversions([2,4,1,3,5]))
assert get_inversions([2,4,1,3,5])[0] == 3
assert get_inversions([5,4,3,2,1])[0] == 10

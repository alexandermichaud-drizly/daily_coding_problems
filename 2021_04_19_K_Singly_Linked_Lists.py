list1 = [3,5,6,11]
list2 = [2,8,9,10,13]
list3 = [1,4,7,12]

lists = [list1,list2,list3]


def merge(a,b):
    merged = []
    while len(a) > 0 or len(b) > 0:
        if len(a) == 0:
            merged += b
            b = []
        elif len(b) == 0:
            merged += a
            a = []
        elif a[0] > b[0]:
            merged.append(b.pop(0))
        else:
            merged.append(a.pop(0))
    return merged

def link_lists(lists):
    while len(lists) > 1:
        print(f'Lists: {lists}')
        merged = merge(lists[0], lists[1])
        lists = [merged] + lists[2:] if len(lists) > 2 else [merged]
    return lists[0]

print(link_lists(lists))

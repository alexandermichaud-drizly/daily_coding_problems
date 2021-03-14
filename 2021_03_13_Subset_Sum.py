test = [12,1,61,5,9,2]

def get_subset_sum(s, k):
    for i in s:
        head = s[0]
        if head == k:
            return [head]
        elif head < k:
            result = get_subset_sum(s[1:], k - head)
            if result is not None:
                return [head] + result 
            else:
                return get_subset_sum(s[1:], k)
        elif len(s) == 1:
            return None
        else:
            return get_subset_sum(s[1:], k)


print(f'Final answer: {get_subset_sum(test, 24)}')
#assert get_subset(test, 24) == [12,1,9,2]

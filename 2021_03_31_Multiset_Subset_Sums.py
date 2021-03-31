test_set = [15,5,20,10,35,15,10]


def partition_with_equal_sums(s, sums=(0,0)):
    if len(s) == 0:
        print(sums)
        return sums[0] == sums[1]

    add_left = (sums[0] + s[0], sums[1])
    add_right = (sums[0], sums[1] + s[0])
    return partition_with_equal_sums(s[1:], add_left) or partition_with_equal_sums(s[1:], add_right)
   
print(partition_with_equal_sums(test_set))

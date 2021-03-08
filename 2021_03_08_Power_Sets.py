test_set = [1,2,3]

def power_set(s):
    output = [[]]
    for i in s:
        temp = [] 
        for j in output:
            item = j.copy()
            item.append(i)
            temp.append(item)
        output += temp
    return output
        
print(power_set(test_set))
# assert power_set(test_set)) == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

from functools import reduce

test = [-10,5,8,2,-6,9,-3]

def largest_product_of_three_elements(arr):
    multipliers = arr[:3]
    largest_product = reduce(lambda x,y: x*y, multipliers) 

    for i in arr[3:]:
        candidates = []
        
        for j in range(3):
            temp = multipliers.copy()
            temp[j] = i
            print(temp)
            candidates.append(temp)

        for k in candidates:
            temp_product = reduce(lambda x,y: x*y, k) 
            if temp_product > largest_product:
                multipliers = k
                largest_product = temp_product
        
    print(multipliers)
    return largest_product

if __name__ == "__main__":
    print(largest_product_of_three_elements(test))

from math import floor

def find_majority_element(lst: list) -> int:
    memo = {}
    half = floor(len(lst) / 2.0)
    for i in lst:
        if i in memo:
            memo[i] += 1
            if memo[i] > half:
                return i
        else:
            memo[i] = 1
            
if __name__ == "__main__":
    print(find_majority_element([1, 2, 1, 1, 3, 4, 1]))
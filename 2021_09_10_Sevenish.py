def sevenish(n: int) -> int:
    sevenish_nums = [7]
    powers_of_seven = [7]

    i = 1
    while len(sevenish_nums) < n - 1:
        next_pow = 7**i
        powers_of_seven.append(next_pow)
        
    return sevenish_nums[-1]


if __name__ == "__main__":
   print(sevenish(3))
   print(sevenish(100))
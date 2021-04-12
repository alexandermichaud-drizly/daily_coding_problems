def nth_perfect(n):
    i = 1
    output = 19

    while i < n:
        temp = output + 9
        digit_sum = sum(list(map(int, str(temp).strip())))
        while digit_sum != 10:
            temp += 9
            digit_sum = sum(list(map(int, str(temp).strip())))
        output = temp
        i += 1

        print(f'i: {i}, n: {output}')

if __name__ == "__main__":
    nth_perfect(100)

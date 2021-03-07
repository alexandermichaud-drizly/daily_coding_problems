def running_median(seq):
    upper = seq[0]
    lower = seq[0]
    median = seq[0]
    output = []

    for i, n in enumerate(seq):
        print(i,n)
        if n > upper:
            if i % 2 == 0:
                median = ( upper + lower ) /2.0
            else:
                median = upper
                upper = n
        elif n < lower:
            if i % 2 == 0:
                median = (upper + lower) / 2.0
            else:
                median = lower
                lower = n
        else:
            if i % 2 == 0:
                if n < median:
                    lower = n
                else:
                    upper = n
                median = ( upper + lower ) / 2.0
            else:
                median = n    

        print(f'Upper: {upper}; Lower: {lower}; Median: {median}')
        output.append(median)

    return output


test_sequence = [2, 1, 5, 7, 2, 0, 5]

print(running_median(test_sequence))
assert running_median(test_sequence) == [2, 1.5, 2, 3.5, 2, 2, 2]

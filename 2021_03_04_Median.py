def running_median(seq):
    if len(seq) == 1:
        return seq
    elif len(seq) == 2:
        return [( seq[0] + seq[1] ) / 2.0]
    elif len(seq) == 3:
        return [seq[1]]

    upper = seq[2]
    lower = seq[0]
    median = seq[1]
    output = [seq[0],( seq[0] + seq[1] ) / 2.0, seq[1]]

    for i, n in enumerate(seq[3:]):
        print(i,n)
        if n > upper:
            if i % 2 == 0:
                lower = median
                median = ( upper + lower ) /2.0
            else:
                median = upper
                upper = n
        elif n < lower:
            if i % 2 == 0:
                upper = median
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
# assert running_median(test_sequence) == [2, 1.5, 2, 3.5, 2, 2, 2]

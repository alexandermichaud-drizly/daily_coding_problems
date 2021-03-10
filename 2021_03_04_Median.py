def running_median(seq):
    upper = seq[0]
    lower = seq[0]
    low_median = seq[0]
    up_median = seq[0]

    for i, n in enumerate(seq):
        if n > upper:
            lower = low_median
            if i % 2 == 0:
                low_median = upper
                up_median = upper
            else:
                low_median = up_median
                up_median = upper
            upper = n
            
        elif n > up_median:
            lower = low_median
            if i % 2 == 0:
                low_median = n
                up_median = n
            else:
                low_median = up_median
                up_median = n

        elif n > low_median:
            
        elif n > lower:


        output.append((upper + lower) / 2.0)

    return output


test_sequence = [2, 1, 5, 7, 2, 0, 5]

print(running_median(test_sequence))
# assert running_median(test_sequence) == [2, 1.5, 2, 3.5, 2, 2, 2]

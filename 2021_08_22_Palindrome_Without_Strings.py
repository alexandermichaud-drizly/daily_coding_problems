def no_conversion_palindrome(n: int) -> bool:
    if n < 10:
        return True
    i = 1
    digits = []
    prev_sum = 0
    running_sum = 0
    while i < n:
        j = n % (i * 10)
        if len(digits) > 0:
            j -= prev_sum
            running_sum += j
            j /= i
        else:
            running_sum += j
        digits.append(int(j))
        i *= 10
        prev_sum = running_sum

    num_digits = len(digits)
    first_half = digits[:(num_digits//2)]
    second_half = digits[(num_digits//2):]
    if num_digits % 2 != 0:
        second_half.pop(0)

    backend = list(reversed(second_half))
    for k, l in enumerate(first_half):
        if l != backend[k]:
            return False
    return True

if __name__ == "__main__":
    assert no_conversion_palindrome(181)
    assert not no_conversion_palindrome(899)
    assert no_conversion_palindrome(888)
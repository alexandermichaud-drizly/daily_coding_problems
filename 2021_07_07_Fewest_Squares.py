from math import sqrt, floor

def fewest_squares(n: int, memo = {}) -> int:
    if n == 1:
        return 1
    if n in memo:
        return memo[n]

    fewest = None

    for i in range(2, floor(n / 2) + 1):
        if i in memo and memo[i] is not None:
            j = fewest_squares(n - i)
            if j is not None:
                k = memo[i] + j
                fewest = min(fewest, k) if fewest is not None else k
        elif i**2 == n:
            memo[n] = 1
            return 1
        else:
            a = fewest_squares(i, memo)
            b = fewest_squares(n - i, memo)
            if a is not None and b is not None:
                c = a + b
                fewest = min(fewest, c) if fewest is not None else c

    memo[n] = fewest
    return fewest 

if __name__ == "__main__":
    assert fewest_squares(4) == 1
    assert fewest_squares(13) == 2
    assert fewest_squares(27) == 3

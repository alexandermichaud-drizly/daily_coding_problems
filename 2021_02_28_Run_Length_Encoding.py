def encode(input):
    encoded = ''
    index = 0
    while index < len(input):
        char = input[index]
        n = 0
        while index < len(input) and input[index] == char:
            n += 1
            index += 1
        encoded += str(n) + char
    return encoded

assert encode("AAAABBBCCDAA") == "4A3B2C1D2A"

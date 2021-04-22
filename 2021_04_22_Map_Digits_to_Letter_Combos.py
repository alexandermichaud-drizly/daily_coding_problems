dpad = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4":["g", "h", "i"]}

def dial(input, dialpad):
    combos = dialpad[input[0]]

    for digit in input[1:]:
        letters = dialpad[digit]
        temp = []
        for i in combos:
            for j in letters:
                temp.append(i + j)
        combos = temp

    return combos

if __name__ == "__main__":
    print(dial("23",dpad))
    print(dial("243",dpad))

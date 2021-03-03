def evenly_space(words, k, l):
    i = 0
    while l < k:
        if i == len(words) - 1: 
            i = 0
        else:
            words[i] += ' ' 
            l += 1
            i += 1
    return words

def justify(words, k):
    lines = []
    temp_line = []
    length_without_spaces = 0
    min_length = 0
    line_complete = False
    index = 0

    while index < len(words):
        word = words[index] 
        if index == len(words) - 1 or min_length + len(word) == k:
            temp_line.append(word)
            length_without_spaces += len(word)
            min_length += len(word)
            line_complete = True
            index += 1

        elif min_length + len(word) > k:
            line_complete = True
        
        else:
            min_length += len(word) if len(temp_line) == 0 else len(word) + 1
            length_without_spaces += len(word)
            temp_line.append(word)
            print(f'Min length: {min_length}; len_w/out_spaces: {length_without_spaces}')
            index += 1

        if line_complete:
            temp_line = evenly_space(temp_line, k, length_without_spaces)
            next_line = ''.join(temp_line)
            lines.append(next_line)
            temp_line = []
            min_length = 0
            length_without_spaces = 0
            line_complete = False


    return lines

test_input = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

print(justify(test_input, 16))

assert justify(test_input, 16) == [\
    "the  quick brown",\
    "fox  jumps  over",\
    "the   lazy   dog"]
    

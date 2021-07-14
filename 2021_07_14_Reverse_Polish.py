import operator
ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv }

def evaluate_reverse_polish(vector: list) -> int:
    print(vector)
    if len(vector) == 1:
        return vector[0]
    
    scanning_operators = False
    for i, e in enumerate(vector):
        if i == len(vector) - 1: 
            output = ops[e](vector[0], evaluate_reverse_polish(vector[1:i]))
            new_vector = [output] + vector[(i + 1):]
            return evaluate_reverse_polish(new_vector)
        elif type(e) is int and scanning_operators == True:
            output = ops[vector[i - 1]](vector[0], evaluate_reverse_polish(vector[1:(i-1)]))
            new_vector = [output] + vector[i:]
            return evaluate_reverse_polish(new_vector)
        elif type(e) is str and scanning_operators == False:
            scanning_operators = True


if __name__ == "__main__":
    test = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
    assert evaluate_reverse_polish(test) == 5
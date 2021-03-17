import random
from matplotlib import pyplot
from collections import Counter

def rand5():
    return random.randint(1,5)

def rand7():
    sum = 0
    for i in range(7):
        sum += rand5()
    remainder = sum % 7
    return 7 if remainder == 0 else remainder


def validate_randomness(tests):
    data = []
    for i in range(tests): 
        data.append(rand7())

    data_counter = Counter(data)
    data_counter_sorted = sorted(data_counter.items())

    probabilities = [i[0] for i in data_counter_sorted] 
    frequency = [i[1] for i in data_counter_sorted] 
    width = 1

    pyplot.bar(probabilities, frequency, width=width)
    pyplot.show()

validate_randomness(100000)

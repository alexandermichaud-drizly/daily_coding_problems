from random import randint

def rand7():
    return randint(1,7)

def rand5():
    sum = 0
    for _ in range(5):
        sum += rand7()

    return (sum % 5) + 1

if __name__ == "__main__":
    for _ in range(20):
        print(rand5())


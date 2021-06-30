from functools import reduce

class Adder:
    def __init__(self, l) -> None:
        self.l = l
        self.length = len(self.l)
        self.total = 0
        self.partial_sums = {} 
        self.preprocess()

    def preprocess(self) -> None:
        self.total = reduce(lambda a,b: a + b, self.l)
        self.partial_sums[(0,0)] = 0
        for i in range(1, self.length):
            self.partial_sums[(0, i)] = self.partial_sums[(0, i - 1)] + self.l[i - 1]
            self.partial_sums[(i, self.length)] = self.total - self.partial_sums[(0, i)]

    def sum(self, i, j) -> int:
        return self.total - self.partial_sums[(0, i)] - self.partial_sums[(j, self.length)]

if __name__ == "__main__":
    test = Adder([1, 2, 3, 4, 5])
    print(test.sum(3, 4))
    print(test.sum(2, 4))
    print(test.sum(0,4))
    print(test.sum(3,3))
    print(test.sum(4,4))


from random import random
from typing import BinaryIO

class CoinToss:
    def __init__(self) -> None:
        self.threshold = random()

    def biased(self) -> BinaryIO:
        return 1 if random() > self.threshold else 0

    def unbiased(self) -> BinaryIO:
        first: BinaryIO = 0
        second: BinaryIO = 0
        while first == second:
            first = self.biased()
            second = self.biased()
        if first == 1:
            return 1
        return 0

if __name__ == "__main__":
    toss = CoinToss()
    print(toss.threshold)
    s = 0
    for _ in range(1000):
        s += toss.biased()
    print(s / 1000)
    s = 0
    for _ in range(1000):
        s += toss.unbiased()
    print(s / 1000)

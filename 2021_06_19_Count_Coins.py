class ChangeCounter:
    def __init__(self, coins: list) -> None:
        self.coins = coins
        self.memo = {}

    def min_coins(self, cents: int) -> int:
        temp_min = None
        for coin in self.coins:
            if coin == cents:
                return 1
            if coin < cents:
                diff = cents - coin
                if diff not in self.memo:
                    self.memo[diff] = self.min_coins(cents - coin)
                temp_min = min(temp_min, self.memo[diff]) if temp_min is not None else self.memo[diff]
        return temp_min + 1 if temp_min is not None else None

if __name__ == "__main__":
    american = ChangeCounter([25,10,5,1])
    print(american.min_coins(25))
    print(american.min_coins(17))
    weird = ChangeCounter([15,11,7,2,1])
    print(weird.min_coins(15))
    print(weird.min_coins(14))
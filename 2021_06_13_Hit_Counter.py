class HitCounter:
    def __init__(self) -> None:
        self.log = []
        self.total = 0

    def record(self, t) -> None:
        if self.total == 0:
            self.log.append(t)
        else:
            i = 0
            while i < self.total and self.log[i] < t:
                i += 1
            self.log.insert(i, t)
        self.total += 1

    def range(self, lower, upper) -> int:
        k = 0
        while k < self.total and self.log[k] < lower:
            k += 1
        j = k
        k += 1
        while k < self.total and self.log[k] < upper:
            k += 1
        return len(self.log[j:k])

if __name__ == "__main__":
    hit_counter = HitCounter()
    hit_counter.record(7)
    hit_counter.record(3)
    hit_counter.record(16)
    hit_counter.record(9)
    hit_counter.total
    print(hit_counter.range(1,17))
    print(hit_counter.range(6,8))
    print(hit_counter.range(7,7))
    print(hit_counter.range(7,9))

# Note: if memory is restricted, HitCounter can dump existing entries when new entries are recorded.
# What to dump depends on usage requirements, but the easiest and most intuitive solution, 
# # given that the data is a vector of timestamps, is to dump the first, i.e. oldest entry.
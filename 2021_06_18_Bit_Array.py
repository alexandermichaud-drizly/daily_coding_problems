from typing import BinaryIO


class BitArray:
    def __init__(self) -> None:
        self.bits = {}

    def set(self, i: int, val=1) -> None:
        if val == 1:
            self.bits[i] = True
        else:
            del self.bits[i]
    
    def get(self, i: int) -> int:
        return 1 if i in self.bits else 0

if __name__ == "__main__":
    bit_array = BitArray()
    bit_array.set(3)
    bit_array.set(4)
    bit_array.set(7)
    bit_array.set(3, 0)
    print(bit_array.get(7))
    print(bit_array.get(4))
    print(bit_array.get(3))
 

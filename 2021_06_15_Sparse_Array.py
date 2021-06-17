class SparseArray:
    def __init__(self, arr: list[int], size: int) -> None:
        self.size = size
        self.obj = {}
        for i, x in enumerate(arr):
            if x != 0:
                self.obj[i] = x
        
    def set(self, i: int, val: int) -> None:
        self.obj[i] = val     
    def get(self, i: int) -> any:
        return self.obj[i] if self.obj[i] else None


if __name__ == "__main__":
    test_list = [0,0,0,4,0,0,0,0,0,0,0,8,9,0,0,0,0,0,0,0,3,0,0,0,0,2,0,0,0,0,0,0,3,0,0,0,0]
    sparseArray = SparseArray(test_list,len(test_list))
    sparseArray.set(1,2)
    sparseArray.set(3,9)
    sparseArray.set(20,7)
    sparseArray.set(14,6)
    sparseArray.get(3)
    print(sparseArray.obj)


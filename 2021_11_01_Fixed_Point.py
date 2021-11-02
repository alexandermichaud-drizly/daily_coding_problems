from typing import Union

def find_fixed_point(arr: list) -> Union[int,bool]:
    for i,x in enumerate(arr):
        if i == x:
            return i
    return False

if __name__ == "__main__":
    print(find_fixed_point([-6, 0, 2, 40]))
    print(find_fixed_point([1, 5, 7, 8]))
   
def can_modify_once(l) -> bool:
    i = 0
    j = 1
    d = 0
    while i < len(l) - 1:
        if l[j] < l[i]:
            d += 1
            if d > 1:
                return False
        i += 1
        j += 1
    return True
        

if __name__ == "__main__":
    assert can_modify_once([1, 3, 5]) == True
    assert can_modify_once([10, 5, 1]) == False
    assert can_modify_once([20, 5, 7]) == True
    assert can_modify_once([1, 4, 3, 7]) == True
    assert can_modify_once([1, 4, 3, 3]) == True
    assert can_modify_once([1, 4, 3, 2]) == False
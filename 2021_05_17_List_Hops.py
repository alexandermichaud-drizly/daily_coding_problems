def hop(hop_list: list) -> bool:
    if len(hop_list) == 1:
        return True
    
    skips = hop_list[0]
    if skips < len(hop_list) and skips != 0:
        for i in range(skips, 0, -1):
            new_list = hop_list[i:]
            if hop(new_list):
                return True
    return False

if __name__ == "__main__":
    print(hop([2,0,1,0]))
    print(hop([1,1,0,1]))
    print(hop([3,0,2,0,1,0]))

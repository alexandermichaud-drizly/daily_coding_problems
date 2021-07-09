def anagram_is_palindrome (s: str) -> bool:
    hash = {}
    for c in s:
        hash[c] = hash[c] + 1 if c in hash else 1
    
    odds = 0
    for k, v in hash.items():
        if v % 2 != 0:
            odds += 1
            if odds > 1:
                return False

    return True

if __name__ == "__main__":
    assert anagram_is_palindrome("carrace")
    assert anagram_is_palindrome("daily") == False
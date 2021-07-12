def first_recurring(s: str):
    store = {}
    for c in s:
        if c not in store:
            store[c] = True
        else:
            return c
    return None

if __name__ == "__main__":
    print(first_recurring("acbbac"))
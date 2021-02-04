def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(c):
    def f(a, b):
        return a
    return c(f)

def cdr(c):
    def f(a, b):
        return b
    return c(f)

assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4

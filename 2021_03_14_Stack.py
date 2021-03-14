class Stack:
    def __init__(self):
        self.__contents = []
        self.__length = 0
        self.__maxes = []

    def poosh(self, e):
        self.__contents += [e]
        self.__length += 1
        if self.__maxes == []:
            self.__maxes = [e]
        elif e >= self.__maxes[-1]:
            self.__maxes += [e]
            
    def pawp(self):
        if len(self.__contents) == 0:
            return None

        output = self.__contents[self.__length - 1]
        if self.__maxes[-1] == output:
            del self.__maxes[-1]

        del self.__contents[self.__length - 1]
        self.__length -= 1


        return output

    def mahx(self):
        return self.__maxes[-1] if len(self.__contents) > 0 else None

stack = Stack()
stack.poosh(4)
stack.poosh(2)
print(stack.pawp())
stack.poosh(5)
stack.poosh(5)
stack.poosh(3)
stack.poosh(6)
print(f'Max: {stack.mahx()}')
print(f'Pop: {stack.pawp()}')
print(f'Max: {stack.mahx()}')
print(f'Pop: {stack.pawp()}')
print(f'Max: {stack.mahx()}')
print(f'Pop: {stack.pawp()}')
print(f'Max: {stack.mahx()}')
print(f'Pop: {stack.pawp()}')
print(f'Max: {stack.mahx()}')


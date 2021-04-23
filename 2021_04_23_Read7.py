test = "This is a test string with 40 characters"

class Reader:
    def __init__(self, s):
        self.s = s
        self.cursor = 0

    def read7(self):
        if self.cursor + 7 > len(self.s):
            output = self.s[self.cursor:]
            self.cursor = len(self.s)
        else:
            output = self.s[self.cursor:self.cursor+7]
            self.cursor += 7
        return output

    def readN(self, n):
        output = ""

        j = n // 7
        for i in range(j + 1):
            output += self.read7()
        
        k = n % 7

        self.cursor -= 7 - k
        output = output[:(7*j)+k]

        return output

        
if __name__ == "__main__":
    reader = Reader(test)
    print(reader.readN(7))
    print(reader.readN(8))
    print(reader.readN(5))
    print(reader.readN(45))

class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        s = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                s += i
        return s == self.Value

    def Factors(self):
        print("Factors:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        s = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                s += i
        return s


obj = Numbers(28)
print("Prime:", obj.ChkPrime())
print("Perfect:", obj.ChkPerfect())
obj.Factors()
print("Sum of Factors:", obj.SumFactors())
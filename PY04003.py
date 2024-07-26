import math
class Fraction:
    tu  = 0
    mau = 0
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def simple(self):
        g = math.gcd(self.tu, self.mau)
        self.tu = self.tu // g
        self.mau = self.mau // g
    def plus(self, a):
        m = self.mau * a.mau
        self.tu = self.tu*a.mau + self.mau*a.tu
        self.mau = m
inp = list(map(int, input().split()))
f1 = Fraction(inp[0], inp[1])
f2 = Fraction(inp[2], inp[3])
f1.plus(f2)
f1.simple()
print(f1.tu, end = "/")
print(f1.mau)
    

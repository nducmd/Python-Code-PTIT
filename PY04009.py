class ComplexNum:
    def __init__ (self, a, b):
        self.a = a
        self.b = b
        
    def plus(self, c2):
        return ComplexNum(self.a + c2.a, self.b + c2.b)
    
    def mul(self, c2):
        c = c2.a
        d = c2.b
        return ComplexNum(self.a*c - self.b*d, self.a*d + self.b*c)
    
    def __str__(self):
        if self.b >= 0:
            return str(self.a) + " + " + str(self.b) + "i"
        return str(self.a) + " - " + str(-1*self.b) + "i"
    
t = int(input())
while t > 0:
    t -= 1
    a,b,c,d = [int(x) for x in input().split()]
    A = ComplexNum(a, b)
    B = ComplexNum(c, d)
    C = A.plus(B)
    C = C.mul(A)
    D = A.plus(B)
    D = D.mul(D)
    print(C, end = ", ")
    print(D)
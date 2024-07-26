import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, k):
        x0 = self.x - k.x
        y0 = self.y - k.y
        return math.sqrt(x0*x0 + y0*y0)
    
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def cnt(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)
        if(max(a, b, c) * 2 >= a + b + c) : print('INVALID')
        else :
            d = a + b + c
            print('{:.3f}'.format(d))
t = int(input())
tt = t
a = []
while t > 0:
    t -= 1
    a += [float(x) for x in input().split()]

i = 0
while tt > 0:
    tt -= 1
    triagle = Triangle(Point(a[0+i], a[1+i]), Point(a[2+i], a[3+i]), Point(a[4+i], a[5+i]))
    triagle.cnt()
    i += 6
    
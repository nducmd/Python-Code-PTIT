class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, a):
        return "{:.4f}".format(((self.x - a.x)*(self.x-a.x) + (self.y-a.y)*(self.y-a.y))**0.5)

def Decimal(n):
    return float(n) 
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
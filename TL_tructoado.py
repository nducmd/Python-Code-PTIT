class Doan:
    a = 0
    b = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __lt__(self, other):
        return self.b < other.b
    def __str__(self):
        return str(self.a) + " " + str(self.b)
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    lst = []
    for i in range(n):
        a, b = [int(x) for x in input().split()]
        lst.append(Doan(a, b))
    lst.sort()
    cnt = 0
    lenm = 0
    for i in lst:
        if i.a >= lenm:
            lenm = i.b
            cnt += 1
            # print(i)
    print(cnt)
    

# 1
# 10
# 39 55
# 37 74
# 0 1
# 19 25
# 65 76
# 51 52
# 19 21
# 5 94
# 46 65
# 32 40
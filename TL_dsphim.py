from datetime import datetime
noTL = 1
noP = 1
class TheLoai:
    def __init__(self, ten):
        self.id = 'TL{:03d}'.format(noTL)
        self.ten = ten
    def __str__(self):
        return self.ten
    
class Phim:
    def __init__(self, maTL, ngay, ten, sotap):
        global noP
        self.id = 'P{:03d}'.format(noP)
        self.ten = ten
        self.maTL = maTL
        self.ngay = ngay
        self.sotap = sotap
        self.nchieu = datetime.strptime(ngay, "%d/%m/%Y")
        noP += 1
    
    def setTL(self, tl):
        self.tentl = tl
    
    def getTL(self):
        return self.maTL
    
    def __str__(self):
        return self.id + " " + self.tentl + " " + self.ngay + " " + self.ten + " " + str(self.sotap)
    
    def __lt__(self, other):
        if self.nchieu == other.nchieu:
            if self.ten == other.ten:
                return self.sotap > self.sotap
            return self.ten < other.ten
        return self.nchieu < other.nchieu
    
n, m = [int(x) for x in input().split()]
dictPhim = {}
a = []
for i in range(n):
    s = input()
    id = 'TL{:03d}'.format(i+1)
    dictPhim[id] = s
for i in range(m):
    tmp = Phim(input(), input(), input(), int(input()))
    tmp.setTL(dictPhim[tmp.getTL()])
    a.append(tmp)
    # print(tmp)
a.sort()
for i in a:
    print(i)

    
# 2 3
# Hai huoc
# Tinh cam
# TL001
# 25/11/2021
# Phim so 1
# 10
# TL001
# 04/12/2021
# Phim so 2
# 15
# TL002
# 25/11/2021
# Phim so 3
# 5
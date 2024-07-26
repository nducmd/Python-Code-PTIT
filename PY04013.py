from datetime import datetime
no = 1
class Mua:
    def __init__(self, ten):
        self.ten = ten
        global no
        self.id = 'T{:02d}'.format(no)
        no += 1
        self.time = 0
        self.mua = 0
    def getTen(self):
        return self.ten
    def update(self, bd, kt, mua):
        a = datetime.strptime(bd, "%H:%M")
        b = datetime.strptime(kt, "%H:%M")
        self.time += ((b-a).seconds / 60)
        self.mua += mua
        self.tb = self.mua / (self.time / 60)
    def __lt__(self, other):
        return self.tb > other.tb
    def __str__(self):
        return self.id + " " + self.ten + " " + '{:.2f}'.format(self.tb)
t = int(input())
ms = set()
a = []
while t > 0:
    t -= 1
    ten = input()
    bd = input()
    kt = input()
    mua = int(input())
    if ten not in ms:
        ms.add(ten)
        a.append(Mua(ten))
    for i in a:
        if i.getTen() == ten:
            i.update(bd, kt, mua)
            break

print(*a, sep="\n")

# 10
# Dong Anh
# 07:30
# 08:00
# 60
# Cau Giay
# 07:45
# 08:12
# 50
# Soc Son
# 08:00
# 09:15
# 78
# Dong Anh
# 18:50
# 20:00
# 88
# Cau Giay
# 19:01
# 20:00
# 77
# Soc Son
# 19:06
# 20:21
# 66
# Dong Anh
# 21:00
# 21:40
# 49
# Cau Giay
# 21:50
# 22:20
# 68
# Dong Anh
# 22:15
# 23:45
# 30
# Cau Giay
# 22:50
# 23:45
# 35
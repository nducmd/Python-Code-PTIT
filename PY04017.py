from datetime import datetime
class Cuaro:
    def __init__(self, ten, donvi, dich):
        self.ten = ten
        self.donvi = donvi
        self.dich = datetime.strptime(dich, "%H:%M")
        self.xuatphat = datetime.strptime("6:00", "%H:%M")
        self.tg = (self.dich - self.xuatphat).seconds / (3600)
        self.vt = 120 / self.tg
        
        tmp = (donvi + " " + ten).split()
        self.ma = ""
        for i in tmp:
            self.ma += i[0].upper()
            
    def __lt__(self, other):
            return self.vt > other.vt
    def __str__(self):
        return self.ma + " " + self.ten + " " + self.donvi + " " + str(round(self.vt)) + " Km/h"
n = int(input())
a = []
for _ in range(n):
    ten = input()
    dv = input()
    dich = input()
    a.append(Cuaro(ten, dv, dich))
a.sort()
for i in a:
    print(i)
    
# 3
# Tran Vu Minh
# Ha Noi
# 8:30
# Vu Ngoc Hoang
# Hoa Binh
# 8:20
# Pham Dinh Tan
# An Giang
# 8:45
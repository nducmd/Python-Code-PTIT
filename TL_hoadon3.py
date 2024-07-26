
class HoaDon:
    def __init__(self, id, ten, sl, dongia, chietkhau):
        self.id = id
        self.ten = ten
        self.sl = sl
        self.dongia = dongia
        self.chietkhau = chietkhau
        self.tien = sl * dongia - chietkhau
        
        
    
    def __lt__(self, other):
        return self.tien > other.tien
    def __str__(self):
        return self.id + " " + self.ten + " " + str(self.sl)  + " " + str(self.dongia) + " " + str(self.chietkhau) + " " + str(self.tien)
    
n = int(input())
lst = []
for i in range(n):
    lst.append(HoaDon(input(), input(), int(input()), int(input()), int(input())))
    
lst.sort()

for i in lst:
    print(i)
    
# 3
# ML01
# May lanh SANYO
# 12
# 4000000
# 2400000
# ML02
# May lanh HITACHI
# 4
# 2550000000
# 0
# ML03
# May lanh NATIONAL
# 5
# 3000000
# 150000
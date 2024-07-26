no = 1
class HoaDon:
    def __init__(self, name, old, new):
        global no
        self.id = 'KH{:02d}'.format(no)
        no += 1
        self.name = name
        self.cnt = new - old
        if self.cnt > 100:
            self.plus = 5
        elif self.cnt >= 51:
            self.plus = 3
        else:
            self.plus = 2
        
        if self.cnt <= 50:
            self.m = self.cnt * 100
        elif self.cnt <= 100:
            self.m = 50*100 + (self.cnt-50) * 150
        else:
            self.m = 50*100 + 50*150 + (self.cnt - 100) * 200
        
        self.m = self.m / 100 * (self.plus + 100)
    
    def __lt__(self, other):
        return self.m > other.m
    def __str__(self):
        return self.id + " " + self.name + " " + str(round(self.m))
    
n = int(input())
lst = []
for i in range(n):
    name = input()
    old = int(input())
    new = int(input())
    lst.append(HoaDon(name, old, new))
    
lst.sort()

for i in lst:
    print(i)
    
# 3
# Le Thi Thanh
# 468
# 500
# Le Duc Cong
# 160
# 230
# Ha Hue Anh
# 410
# 612
no = 1
class NhanVien:
    def __init__(self, name, lt, th):
        global no
        self.id = 'TS{:02d}'.format(no)
        no +=1
        self.name = name
        if lt > 10:
            lt = lt / 10
        if th > 10:
            th = th / 10
        self.d = (lt + th) / 2
        if self.d < 5 : self.l = 'TRUOT'
        elif self.d < 8 : self.l = 'CAN NHAC'
        elif self.d < 9.5 : self.l = 'DAT'
        else : self.l = 'XUAT SAC'
    def __lt__(self, other):
        return self.d > other.d
    def __str__(self):
        return self.id + " " + self.name + " " + '{:.2f}'.format(self.d) + " " + self.l

n = int(input())
lst = []
for i in range(n):
    name = input()
    old = float(input())
    new = float(input())
    lst.append(NhanVien(name, old, new))
    
lst.sort()

for i in lst:
    print(i)
    
# 3
# Nguyen Thai Binh
# 45
# 75
# Le Cong Hoa
# 4
# 4.5
# Phan Van Duc
# 56
# 56
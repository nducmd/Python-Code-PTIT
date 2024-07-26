import math

no = 1
class Student:
    def __init__(self, name, d1, d2, d3, d4, d5,d6,d7,d8,d9,d10):
        global no
        self.msv = 'HS{:02d}'.format(no)
        no += 1
        self.name = name
        self.diem = (d1 + d2 +d3 + d4 +d5+d6+d7+d8+d9+d10+d1+d2) / 12
        
        if self.diem >=9:
            self.note = "XUAT SAC"
        elif self.diem >= 8:
            self.note = "GIOI"
        elif self.diem >= 7:
            self.note = "KHA"
        elif self.diem >= 5:
            self.note = "TB"
        else:
            self.note = "YEU"
        #self.diem = round(self.diem, 2)
        self.diem = round((self.diem + 0.005) * 10) / 10
    def __lt__(self, other):
        if self.diem == other.diem:
            return self.msv < other.msv
        return self.diem > other.diem
    def __str__(self):
        return self.msv + " " + self.name + " " + '{:.1f}'.format(self.diem) + " " + self.note

n = int(input())
lst = []
for i in range(n):
    name = input()
    d1, d2, d3, d4, d5,d6,d7,d8,d9,d10 = [float(x) for x in input().split()]
    s = Student(name, d1, d2, d3, d4, d5,d6,d7,d8,d9,d10)
    lst.append(s)

lst.sort()

for i in lst:
    print(i)

# 3
# Luu Thuy Nhi
# 9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
# Le Van Tam
# 8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
# Nguyen Thai Binh
# 9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
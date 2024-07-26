import math
no = 1
class Student:
    def __init__(self, ten, d1, d2, d3):
        global no
        self.id = 'SV{:02d}'.format(no)
        no += 1
        
        tmp = ""
        a = ten.split()
        for i in a:
            tmp += i.title() + " "
        self.ten = tmp[0:-1]
        self.tb = math.ceil((d1*3 + d2*3 + d3*2) / (3+3+2) * 100) / 100
    def __lt__(self, other):
        if self.tb == other.tb:
            return self.id < other.id
        return self.tb > other.tb
    def __str__(self):
        return self.id + " " + self.ten + " " + '{:.2f}'.format(self.tb)
    def getTb(self):
        return self.tb
    
t = int(input())
a = []
while t > 0:
    t -= 1
    ten = input()
    d1 = float(input())
    d2 = float(input())
    d3 = float(input())
    a.append(Student(ten, d1, d2, d3))
k = 0
b = 1
d = 0.0
a.sort()
for i in a:
    print(i, end = " ")
    if i.getTb() != d:
        k += b
        d = i.getTb()
        print(k)
        b = 1
    else:
        print(k)
        b += 1
        
# 3
#  ha Thi kieu     anh
# 7
# 6
# 7
# Pham    THI  HAaO
# 6
# 7
# 6
# Pham    THI  HAO
# 7
# 6
# 7
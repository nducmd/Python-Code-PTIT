class Student:
    def __init__(self, msv, ten, lop):
        self.msv = msv
        self.ten = ten
        self.lop = lop
    def setDiem(self, s):
        diem = 10
        for i in s:
            if i == 'v':
                diem -= 2
            elif i == 'm':
                diem -= 1
        self.diem = max(0, diem)
    def __str__(self):
        tt = ""
        if self.diem == 0:
            tt = "KDDK"
        return self.msv + " " + self.ten + " " + self.lop + " " + str(self.diem) + " " + tt
    def getMsv(self):
        return self.msv
    
a = []
n = int(input())
for _ in range(n):
    msv = input()
    ten = input()
    lop = input()
    a.append(Student(msv, ten, lop))

for _ in range(n):
    msv, cc = input().split()
    for i in a:
        if i.getMsv() == msv:
            i.setDiem(cc)
            break

for i in a:
    print(i)

# 3
# B19DCCN999
# Le Cong Minh
# D19CQAT02-B
# B19DCCN998
# Tran Truong Giang
# D19CQAT02-B
# B19DCCN997
# Nguyen Tuan Anh
# D19CQCN04-B
# B19DCCN998 xxxmxmmvmx
# B19DCCN997 xmxmxxxvxx
# B19DCCN999 xvxmxmmvvm
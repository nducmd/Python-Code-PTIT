class Student:
    msv = ""
    name = ""
    lop = ""
    dcc = 0
    note = ""
    def __init__(self, msv, name, lop):
        self.msv = msv
        self.name = name
        self.lop = lop
    def cnt(self, s):
        d = 10
        for i in s:
            if i == 'v':
                d -= 2
            elif i == 'm':
                d -= 1
        self.dcc = d


n = int(input())
lst = []
for i in range(n):
    s = Student(input(), input(), input())
    lst.append(s)

for i in range(n):
    inp = input().split()
    for j in range(n):
        if lst[j].msv == inp[0]:
            lst[j].cnt(inp[1])

for i in range(n):
    if (lst[i].dcc > 0):
        print(lst[i].msv, lst[i].name, lst[i].lop, lst[i].dcc)
    else:
        print(lst[i].msv, lst[i].name, lst[i].lop,0, "KDDK")


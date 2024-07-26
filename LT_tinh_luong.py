def getX(id):
    x = id[0]
    y = int(id[1:3])
    if x == 'A':
        if y >= 16:
            return 20
        elif y >= 9:
            return 14
        elif y >= 4:
            return 12
        else:
            return 10
    elif x == 'B':
        if y >= 16:
            return 16
        elif y >= 9:
            return 13
        elif y >= 4:
            return 11
        else:
            return 10
    elif x == 'C':
        if y >= 16:
            return 14
        elif y >= 9:
            return 12
        elif y >= 4:
            return 10
        else:
            return 9
    else:
        if y >= 16:
            return 13
        elif y >= 9:
            return 11
        elif y >= 4:
            return 9
        else:
            return 8
class NhanVien:
    def __init__(self, id, name, noDate, noSalary):
        self.id = id
        self.de = id[-2:]
        self.name = name
        self.salary = noDate * noSalary * getX(id) * 1000
    def __str__(self):
        return self.id + " " + self.name + " " + self.de + str(self.salary)
    
n = int(input())
mp = {}
for i in range(n):
    s = input().split()
    x = ""
    for j in range(1, len(s)):
        x += s[j] + " "
    mp[s[0]] = x

m = int(input())
for _ in range(m):
    a = NhanVien(input(), input(), int(input()), int(input()))
    a.de = mp[a.de]
    print(a)
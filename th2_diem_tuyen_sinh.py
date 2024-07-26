no = 1
def standard(name):
    s = name.strip().lower().split()
    x = ""
    for i in range(len(s)):
        x += s[i].title() + " "
    return x
def getDt(s):
    if s == 'Kinh':
        return 0
    return 1.5
def getKv(n):
    if n == 1:
        return 1.5
    if n == 2:
        return 1
    return 0
class TS:
    def __init__(self, name, diem, dt, kv):
        global no
        self.id = 'TS{:02d}'.format(no)
        no += 1
        self.ten = standard(name)
        self.diem = diem + getDt(dt) + getKv(kv)
        if self.diem >= 20.5:
            self.note = 'Do'
        else:
            self.note = 'Truot'
            
    def __lt__(self, other):
        if self.diem == other.diem:
            return self.id < other.id
        return self.diem > other.diem
    def __str__(self):
        return self.id + " " + self.ten  + '{:.1f}'.format(self.diem) + " " + self.note
    
n = int(input())
a = []
for i in range(n):
    s = TS(input(), float(input()), input(), int(input()))
    a.append(s)

a.sort()
for i in a:
    print(i)
        
        
# 2
# Nguyen  hong ngat
# 22
# Kinh
# 1
#   Chu thi MINh
# 14
# Dao
# 3
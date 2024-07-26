from datetime import datetime
class Gamer:
    def __init__(self, id, name, o, n):
        self.id = id
        self.name = name
        start_time = datetime.strptime(o, '%H:%M')
        end_time = datetime.strptime(n, '%H:%M')
        delta_time = (end_time - start_time).total_seconds() / 60
        self.h = int((delta_time / 60))
        self.m = delta_time - self.h * 60
        self.d = delta_time
    def __lt__ (self, other):
        return self.d > other.d
    def __str__(self):
        return self.id + " " + self.name + " " + str(self.h) +" gio " + str(int(self.m)) + " phut"
    
n = int(input())
lst = []
for i in range(n):
    id = input()
    name = input()
    o = input()
    n = input()
    lst.append(Gamer(id, name, o, n))
    
lst.sort()
for i in lst:
    print(i)
    
# 3
# 01T
# Nguyen Van An
# 09:00
# 10:30
# 06T
# Hoang Van Nam
# 15:30
# 18:00
# 02I
# Tran Hoa Binh
# 09:05
# 10:00
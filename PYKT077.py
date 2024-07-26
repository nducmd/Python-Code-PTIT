from datetime import datetime
no = 1
class Mon:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten
    def getMa(self):
        return self.ma
    def getTen(self):
        return self.ten
    def __str__(self):
        return self.ma + " " + self.ten
    
class Lich:
    def __init__(self, ma, ngay, gio):
        global no
        self.id = 'T{:03d}'.format(no)
        no += 1
        self.ma = ma
        self.ngay = datetime.strptime(ngay, "%d/%m/%Y")
        self.gio = datetime.strptime(gio, "%H:%M %S")
    def setTen(self, ten):
        self.ten = ten
    def __lt__(self, other):
        if self.ngay == other.ngay:
            if self.gio == other.gio:
                return self.id < other.id
            return self.gio < other.gio
        return self.ngay < other.ngay
    def __str__(self):
        return self.id + " " + self.ma + " " + self.ten + " " + self.ngay.strftime("%d/%m/%Y") + " " + self.gio.strftime("%H:%M %S")
    
n, m = [int(x) for x in input().split()]
a = []
b = []
for _ in range(n):
    ma = input()
    ten = input()
    a.append(Mon(ma, ten))

for _ in range(m):
    inp = input().split()
    ma = inp[0]
    ngay = inp[1]
    gio = inp[2] + " " + inp[3]
    tmp = Lich(ma, ngay, gio)
    for i in a:
        if i.getMa() == ma:
            tmp.setTen(i.getTen())
            break
    b.append(tmp)
b.sort()
print(*b, sep="\n")

# 2 10
# INT1155
# Tin hoc co so 2
# INT1339
# Ngon ngu lap trinh C++
# INT1155 25/11/2021 08:00 01
# INT1155 04/12/2021 08:00 02
# INT1155 04/12/2021 13:30 03
# INT1155 25/11/2021 13:30 04
# INT1155 25/11/2021 15:00 05
# INT1339 25/11/2021 08:00 01
# INT1339 25/11/2021 08:00 02
# INT1339 04/12/2021 13:30 03
# INT1339 04/12/2021 13:30 04
# INT1339 04/12/2021 15:00 05
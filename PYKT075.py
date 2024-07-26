class Danhba:
    def __init__(self, ten, sdt, ngay):
        self.ten = ten
        self.sdt = sdt
        self.ngay = ngay
    def __str__(self):
        return self.ten + ": " + self.sdt + " " + self.ngay
    def __lt__(self, other):
        a = self.ten.split()[-1]
        b = other.ten.split()[-1]
        if a == b:
            return self.ten < other.ten
        return a < b
    
sotay = open('SOTAY.txt')
prev = ""
a = []
tmp = []
for line in sotay:
    s = line.strip().split()
    if s[0] == 'Ngay':
        prev = s[1]
    else:
        tmp.append(line.strip())
        if len(tmp) == 2:
            a.append(Danhba(tmp[0], tmp[1], prev))
            tmp.clear()
db = open('DIENTHOAI.txt', 'w')
for i in a:
    db.write(str(i) + '\n')
db.close()
        
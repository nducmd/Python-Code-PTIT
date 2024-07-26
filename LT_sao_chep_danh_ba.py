

class DanhBa:
    def __init__(self, date, name, phone):
        tmp = date.split()
        tmpn = name.split()
        self.fname = tmpn[-1]
        self.date = tmp[1]
        self.name = name
        self.phone = phone
    def __str__(self):
        return self.name + ': ' + self.phone + " " + self.date
    def __lt__(self, other):
        if self.fname == other.fname:
            return self.name < other.name
        return self.fname < other.fname
    
sotay = open('SOTAY.txt')
dienthoai = open("DIENTHOAI.txt", 'w')
a = []
tmp = []
prev = ""
for line in sotay:
    s = line.strip()
    if len(tmp) == 0:
        if s.startswith("Ngay"):
            prev = s
        else:
            tmp.append(prev)
    tmp.append(s)
    if len(tmp) == 3:
        a.append(DanhBa(tmp[0], tmp[1], tmp[2]))
        tmp.clear()
    
for i in a:
    dienthoai.write(str(i) + "\n")
    
dienthoai.close()

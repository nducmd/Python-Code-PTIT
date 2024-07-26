from datetime import datetime
no = 1
class HoaDon:
    def __init__(self, ten, phong, vao, ra, dv):
        global no
        self.id = 'KH{:02d}'.format(no)
        no += 1
        self.phong = phong
        self.ten = ten
        self.indate = datetime.strptime(vao, "%d/%m/%Y")
        self.outdate = datetime.strptime(ra, "%d/%m/%Y")
        self.dur = int((self.outdate - self.indate).days + 1)
        self.tien = 0
        if phong[0] == '1':
            self.tien = 25 * self.dur + dv
        elif phong[0] == '2':
            self.tien = 34 * self.dur + dv
        elif phong[0] == '3':
            self.tien = 50 * self.dur + dv
        else:
            self.tien = 80 * self.dur + dv

    def __lt__(self, other):
        return self.tien > other.tien
    def __str__(self):
        return self.id + " " + self.ten + " " + self.phong + " " + str(self.dur) + " " + str(self.tien)
        
n = int(input())
lst = []
for i in range(n):
    ten = input().strip()
    phong = input().strip()
    vao = input().strip()
    ra = input().strip()
    dv = int(input().strip())
    #lst.append(HoaDon(input(), input(), input(), input(), int(input())))
    lst.append(HoaDon(ten, phong, vao, ra, dv))

lst.sort()

for i in lst:
    print(i)
    
# 3
# Huynh Van Thanh   
# 103 
# 05/06/2010   
# 05/06/2010   
# 15
# Le Duc Cong  
# 106 
# 08/03/2010   
# 01/05/2010   
# 220
# Tran Thi Bich Tuyen   
# 207 
# 10/04/2010   
# 21/04/2010   
# 96
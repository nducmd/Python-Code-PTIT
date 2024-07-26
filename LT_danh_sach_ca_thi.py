from datetime import datetime

no = 1

class Shift:
    
    def __init__ (self, date, hour, room):
        global no
        self.id = 'C{:03d}'.format(no)
        no += 1
        self.date = date
        self.hour = hour
        self.room = room
        self.d = datetime.strptime(date + " " + hour, '%d/%m/%Y %H:%M')
    def __str__ (self):
        return self.id + " " + self.date + " " + self.hour + " " + self.room
    
    def __lt__ (self, other):
        if self.d == other.d:
            return self.id < other.id
        return self.d < other.d
    
t = int(input())
a = []
while t > 0:
    t -= 1
    s = Shift(input(), input(), input())
    a.append(s)
a.sort()
for i in a:
    print(i)

# 3
# 09/01/2022
# 10:00
# 70279
# 09/01/2022
# 10:00
# 70279
# 09/01/2022
# 09:30
# 70172
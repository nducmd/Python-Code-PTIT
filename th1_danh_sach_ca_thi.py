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
        
    def __lt__(self, other):
        if self.d == other.d:
            return self.id < other.id
        return self.d < other.d
    
    def __str__(self):
        return self.id + " " + self.date + " " + self.hour + " " + self.room
    
    
shiftList = open('CATHI.in')
t = int(shiftList.readline().strip())
lst = []
while t > 0:
    t -= 1
    date = shiftList.readline().strip()
    hour = shiftList.readline().strip()
    room = shiftList.readline().strip()
    lst.append(Shift(date, hour, room))

lst.sort()
for i in lst:
    print(i)
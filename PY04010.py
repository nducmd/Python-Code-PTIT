class Student:
    dob = ""
    name = ""
    diem1 = 0.0
    diem2 = 0.0
    diem3 = 0.0
    diemtb = 0.0
    def __init__(self, name, dob, diem1, diem2, diem3):
        self.name = name
        self.dob = dob
        self.diemtb = diem1 + diem2 + diem3
    def sout(self):
        print(self.name, end = " ")
        print(self.dob, end = " ")
        print(self.diemtb)


s = Student(input(), input(), float(input()), float(input()), float(input()))
s.sout()
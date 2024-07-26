class Student:
    def __init__(self, name, ac, sub):
        self.name = name
        self.ac = ac
        self.sub = sub
    
    def __lt__(self, other):
        if self.ac == other.ac:
            if self.sub == other.sub:
                return self.name < other.name
            else:
                return self.sub < other.sub
        else:
            return self.ac > other.ac
    
    def __str__(self):
        return self.name + " " + str(self.ac) + " " + str(self.sub)
    
n = int(input())
a = []
for i in range(n):
    name = input()
    ac, sub = [int(x) for x in input().split()]
    a.append(Student(name, ac, sub))
a.sort()
for i in a:
    print(i)
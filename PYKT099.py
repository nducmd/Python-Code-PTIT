file1 = open("DATA1.in")
file2 = open("DATA2.in")
a = set()
b = set()
for line in file1:
    for i in line.strip().lower().split():
        a.add(i)
for line in file2:
    for i in line.strip().lower().split():
        b.add(i)
        
for i in sorted(a):
    if i not in b:
        print(i, end = " ")
print()
for i in sorted(b):
    if i not in a:
        print(i, end = " ")
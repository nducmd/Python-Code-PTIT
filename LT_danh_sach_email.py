file_a = open('_a.txt')
a = set()
for line in file_a:
    s = line.strip()
    a.add(s.lower())
b = list(a)
b.sort() 
print(b)    
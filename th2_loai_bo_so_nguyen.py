a = []
with open('DATA.in') as fi:
    for line in fi:
        s = line.strip().split()
        for i in s:
            try:
                n = int(i)
                if n >= 2147483647:
                    a.append(i)
            except:
                a.append(i)
a.sort()
for i in a:
    print(i, end = " ")
    
    
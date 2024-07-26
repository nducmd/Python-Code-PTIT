data = open("DATA.in")
res = []
for line in data:
    s = line.strip()
    a = s.split()
    for i in a:
        try:
            j = int(i)
            if j > 2000000000:
                raise ValueError("")
        except:
            res.append(i)
res.sort() 
for i in res:
    print(i, end = " ")
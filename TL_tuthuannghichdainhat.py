def isTN(s):
    return s == s[::-1]

vanban = open('VANBAN.in')
a = []
m = {}
lenm = 0
for line in vanban:
    s = line.strip()
    for x in s.split():
        if isTN(x):
            if len(x) >= lenm:
                lenm = len(x)
                if x in m:
                    m[x] += 1
                else:
                    m[x] = 1
                    a.append(x)
                    
for x in a:
    if len(x) == lenm:
        print(x, m[x])
        
                
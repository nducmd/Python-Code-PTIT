t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    m ={}
    res = 0
    for i in range(n):
        x = int(input())
        if x in m:
            m[x] += 1
        else:
            m[x] = 1
        res = max(res, m[x])
    a = []
    for x, y in m.items():
        if y == res:
            a.append(x)

    a.sort()
    print(a[0])



t = int(input())
while t > 0:
    t -= 1
    lst = list(map(str, input().split()))
    p = lst[0]
    q = lst[1]
    s = input().split()
    if (len(s) > 1):
        m, n = s[0], s[1]
    else:
        m = s[0]
        n = input()

    a = m.replace(p,q)
    b = n.replace(p,q)
    res1 = int(a) + int(b)
    a = m.replace(q,p)
    b = n.replace(q,p)
    res2 = int(a) + int(b)
    print(min(res1, res2), max(res2, res1))

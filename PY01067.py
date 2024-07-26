def check(s):
    cnt = 0
    for i in s:
        if i == "2":
            cnt += 1
    return cnt > (len(s)/2)

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    ms = set()
    qu = []
    s = "012"
    cnt = 0
    qu.append("0")
    qu.append("1")
    qu.append("2")
    while len(qu) > 0:
        top = qu[0]
        qu.pop(0)
        if check(top) and top not in ms:
            cnt += 1
            print(top, end = " ")
            ms.add(top)
            if cnt == n:
                break
        for i in s:
            qu.append(str(int(top + i)))
    print()
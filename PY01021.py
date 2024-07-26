t = int(input())
while t > 0:
    t -= 1
    a = []
    b = []
    s = input()
    for i in s:
        if i.isdigit():
            b.append(int(i))
        else:
            a.append(i)
    a.sort()
    cnt = sum(b)
    for i in a:
        print(i, end="")
    print(cnt)
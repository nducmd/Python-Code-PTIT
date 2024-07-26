def findMax(s):
    x = ""
    res = 0
    for c in s:
        if c.isnumeric():
            x += c
        elif len(x) != 0:
            a = int(x)
            res = max(res, a)
            x = ""
    if len(x) != 0:
        a = int(x)
        res = max(res, a)
        x = ""
    return res
t = int(input())
while t > 0:
    t -= 1
    s = input()
    print(findMax(s))

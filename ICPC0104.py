def findMin(s):
    x = ""
    res = 999999999999
    for c in s:
        if c.isnumeric():
            x += c
        elif len(x) != 0:
            a = int(x)
            res = min(res, a)
            x = ""
    return res
t = int(input())
while t > 0:
    t -= 1
    s = input()
    print(findMin(s))

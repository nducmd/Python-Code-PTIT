def proc(s):
    st = ""
    res = ""
    for c in s:
        if len(st) == 0:
            st = st + c
            f = 1
        elif c == st[-1]:
            f += 1
        elif st[-1] != c:
            res = res + str(f) + st[-1]
            st = ""
            st = st + c
            f = 1
    res = res + str(f) + st[-1]
    print(res)

t = int(input())
while t > 0:
    inp = input()
    proc(inp)
    t -= 1
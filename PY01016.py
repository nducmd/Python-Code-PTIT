def proc(str):
    i = 1
    while i < len(str):
        f = int(str[i])
        c = str[i-1]
        while f > 0:
            print(c, end = "")
            f -= 1
        i += 2

t = int(input())
while t > 0:
    str = input()
    proc(str)
    print()
    t -= 1
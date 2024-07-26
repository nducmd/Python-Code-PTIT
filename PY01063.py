def cnt(x, s):
    c = 0
    while (s.find(x) != -1):
        c += 1
        i = s.find(x)
        s = s[:i] + s[i+len(x):]
    print(c)

t = int(input())
while t > 0:
    s = input()
    x = input()
    cnt(x, s)
    t -= 1
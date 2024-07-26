def change(r, b):
    if b != 16:
        return str(r)
    if r < 10:
        return str(r)
    if r == 10:
        return "A"
    if r == 11:
        return "B"
    if r == 12:
        return "C"
    if r == 13:
        return "D"
    if r == 14:
        return "E"
    if r == 15:
        return "F"

t = int(input())
while t > 0:
    t -= 1
    b = int(input())
    s = input()
    s = s[::-1]
    m = 0
    for i in range(0, len(s)):
        if s[i] != '0':
            m += 2**i

    res = ""
    while m > 0:
        r = int(m % b)
        res += change(r, b)
        m = m // b
    print(res[::-1])
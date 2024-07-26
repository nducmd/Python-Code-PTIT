t = int(input())
while t > 0:
    t -= 1
    n = input()
    n = n[::-1]
    res = ""
    d = 0
    for i in range(0, len(n) -1):
        tmp = int(n[i]) + d
        if tmp >= 5:
            d = 1
        else:
            d = 0
        res += '0'
    if d > 0:
        tmp = int(n[-1]) + d
        if tmp > 9:
            res += '01'
        else:
            res += str(tmp)
    else:
        res += n[-1]        
    print(res[::-1])
        
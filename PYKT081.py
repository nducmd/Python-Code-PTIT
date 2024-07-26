t = int(input())
while  t > 0:
    t -= 1
    s = input().split('.')
    res = ''
    if len(s) > 4:
        res = 'NO'
    else:
        res = 'YES'
        for i in range(4):
            try:
                if not 0 <= int(s[i]) <= 255:
                    res = 'NO'
                    break
            except:
                res = 'NO'
    print(res)
    
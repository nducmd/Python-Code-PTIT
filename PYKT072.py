n = int(input())
a = []
for i in range(n):
    a.append(input())
    
res = 1e9
for i in range(n):
    s = a[i]
    cnt = 0
    for j in range(n):
        tmp = 0
        x = a[j]
        while s != x:
            x = x[1:] + x[0]
            tmp += 1
            if tmp > len(x):
                break
        if tmp > len(x):
            res = -1
            break
        else:
            cnt += tmp
    if res == -1:
        break
    else:
        res = min(res, cnt)
print(res)


# 2
# molzv
# lzvmo
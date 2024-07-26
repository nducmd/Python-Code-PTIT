t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [0] * n
    b = [0] * n
    f = [1] * n
    res = 1
    for i in range(n):
        a[i], b[i] = [float(x) for x in input().split()]
    for i in range(0, n):
        for j in range(i):
            if a[i] > a[j] and b[i] < b[j]:
                f[i] = max(f[i], f[j] + 1)
            res = max(res, f[i])
    print(res)
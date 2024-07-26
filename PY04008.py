t = int(input())
while t > 0:
    t -= 1
    n, m = [int(x) for x in input().split()]
    inp = []
    for i in range(n):
        inp += [int(x) for x in input().split()]
    a = []
    for i in range(n):
        a.append([0]*m)
    k = 0
    for i in range(n):
        for j in range(m):
            a[i][j] = inp[k]
            k+=1
    b = []
    for i in range(m):
        b.append([0]*n)
    for i in range(n):
        for j in range(m):
            b[j][i] = a[i][j]
    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(m):
                tmp += a[i][k] * b[k][j]
            print(tmp, end = " ")
        print()

t = int(input())
while t > 0:
    t -= 1
    lst = list(map(int,input().split()))
    n = lst[0]
    m = lst[1]
    a=[]
    for i in range(n):
       a.append(list(map(int, input().split())))
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

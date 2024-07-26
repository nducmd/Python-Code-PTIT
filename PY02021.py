t = int(input())
while t > 0:
    t -= 1
    n,m,p = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    flag = 0
    i = 0
    j = 0
    k = 0
    while i < n and j < m and k < p:
        if (a[i] == b[j] and b[j] == c[k]):
            print(a[i], end = " ")
            i += 1
            j += 1
            k += 1
            flag = 1
        while (i < n and j < m and k < p and (a[i] < b[j] or a[i] < c[k])):
            i += 1
        while (i < n and j < m and k < p and (b[j] < a[i] or b[j] < c[k])):
            j += 1
        while (i < n and j < m and k < p and (c[k] < b[j] or c[k] < a[i])):
            k += 1
    if flag == 0:
        print("NO")
    else:
        print()
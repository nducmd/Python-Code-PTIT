t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [int(x) for x in input().split()]
    m = [-1] * n
    m[0] = a[0]
    for i in range (1, n):
        m[i] = max(a[i], m[i-1])
    #print(m)
    M = [1e9] * n
    M[n-1] = a[n-1]
    for i in range (n-2, -1, -1):
        M[i] = min(M[i+1], a[i])
    #print(M)
    cnt = 0
    for i in range(n):
        if m[i] <= a[i] and a[i] <= M[i]:
            cnt += 1
    print(cnt)
    
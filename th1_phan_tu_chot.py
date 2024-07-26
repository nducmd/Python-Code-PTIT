t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [-1]
    a += [int(x) for x in input().split()]
    a.append(1e9)
    
    m = [-1] * (n+2)
    for i in range(1, n+1):
        m[i] = max(m[i-1], a[i-1])
        
    #print(m)
    M = [1e9] * (n+2)
    for i in range(n, 0, -1):
        M[i] = min(M[i+1], a[i+1])
    #print(M)
    
    res = 0
    for i in range(1,n+1):
        if m[i] <= a[i] and a[i] < M[i]:
            res += 1
    
    print(res)
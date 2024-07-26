t = int(input())
while t > 0:
    t -= 1
    n,m,k = [int(x) for x in input().split()]
    a = []
    row = [0] * (m+2)
    a.append(row)
    for i in range(n):
        row = [0] + [int(x) for x in input().split()]
        a.append(row)
    for i in range(1,n+1):
        for j in range(1,m+1):
            a[i][j] = a[i][j] + a[i-1][j] + a[i][j-1] - a[i-1][j-1]
       
    # for i in range(n+1):
    #     for j in range(m+1):
    #         print(a[i][j], end = " ")
    #     print("")
    
    for i in range(k//2+1, n+1-k//2):
        for j in range(k//2+1, m+1-k//2):
            # print(i, j)
            # print(a[i+k//2][j+k//2], a[i-k//2-1][j+k//2], a[i+k//2][j-k//2-1], a[i-k//2-1][j-k//2-1])
            tmp = a[i+k//2][j+k//2] - a[i-k//2-1][j+k//2] - a[i+k//2][j-k//2-1] + a[i-k//2-1][j-k//2-1]
            print(int(tmp / (k*k)), end = " ")
        print("")
    
    # for i in range(1, n - k + 2):
    #     for j in range(1, m - k + 2):
    #         kk = a[i + k - 1][j + k - 1] - a[i - 1][j + k - 1] - a[i + k - 1][j - 1] + a[i - 1][j - 1]
            
    #         print(int(kk/(k*k)), end=" ")
    #     print()
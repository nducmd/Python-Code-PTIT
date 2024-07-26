t = int(input())
while t > 0:
    t -= 1
    n, m, l = [int(x) for x in input().split()]
    a = [[0] * (m+1)] * (n+1)
    b = [[1] * l] * l
    c = [[0] * (m+1)] * (n+1)
    for i in range(1,n+1):
        a[i] = [0] + [int(x) for x in input().split()]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a[i][j] += a[i][j - 1] + a[i - 1][j] - a[i - 1][j - 1]
    for i in range(1, n - l + 2):
        for j in range(1, m - l + 2):
            k = a[i + l - 1][j + l - 1] - a[i - 1][j + l - 1] - a[i + l - 1][j - 1] + a[i - 1][j - 1]
            
            print(int(k/(l*l)), end=" ")
        print()
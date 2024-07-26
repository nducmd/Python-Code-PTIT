t = int(input())
while t > 0:
    t -= 1
    n, m = [int(x) for x in input().split()]
    a = [[]] * n
    b = [[]] * 3
    for i in range(n):
        a[i] = [int(x) for x in input().split()]
    for i in range(3):
        b[i] = [int(x) for x in input().split()]
    res = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            res += a[i-1][j-1] * b[0][0]
            res += a[i-1][j] * b[0][1]
            res += a[i-1][j+1] * b[0][2]
            res += a[i][j-1] * b[1][0]
            res += a[i][j] * b[1][1]
            res += a[i][j+1] * b[1][2]
            res += a[i+1][j-1] * b[2][0]
            res += a[i+1][j] * b[2][1]
            res += a[i+1][j+1] * b[2][2]

    print(res) 


# 2
# 4 4
# 2 1 0 0
# 3 2 1 1
# 4 3 2 1
# 2 2 1 0
# -1 -1 -1
# -1 8 -1
# -1 -1 -1
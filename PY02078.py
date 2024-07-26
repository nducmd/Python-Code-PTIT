t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [0.0]*n
    b = [0.0]*n
    for i in range(n):
        a[i], b[i] = [float(x) for x in input().split()]
        
    res = 1
    f = [1] * (n+1)
    for i in range(n):
        for j in range(0,i):
            if a[j] < a[i] and b[j] > b[i]:
                f[i] = max(f[i], f[j] + 1)
                res = max(f[i], res)
    print(res)
    
    
# 3
# 2
# 1.0 1.0
# 1.5 0.0
# 3
# 1.0 1.0
# 1.0 1.0
# 1.0 1.0
# 6
# 1.5 9.0
# 2.0 2.0
# 2.5 6.0
# 3.0 5.0
# 4.0 2.0
# 10.0 5.5
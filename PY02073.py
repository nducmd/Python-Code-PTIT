t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    x, y, z = [int(x) for x in input().split()]
    f = [10**5 for i in range(n+1)]
    f[0] = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            f[i] = min(f[i-1] + x, f[i//2] + z)
        else:
            f[i] = min(f[i-1] + x, f[(i-1)//2] + z + x, f[(i+1)//2] + z + y)
    print(f[n])
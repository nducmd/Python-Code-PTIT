t = int(input())
while t > 0:
    t -= 1
    n,p = [int(x) for x in input().split()]
    res = 0
    while n > 0:
        tmp = n
        while tmp % p == 0:
            tmp //= p
            res += 1
        n -= 1
    print(res)
t = int(input())
while t > 0:
    t -= 1
    n,m = [int(x) for x in input().split()]
    x = input()
    ms = set()
    for c in x:
        ms.add(c)
    k = n - len(x)
    res = 1
    if k == 0:
        print(1)
    else:
        
        for i in range(1, k+2):
            res = res * i
            res = res % m
        print(res*26)
def calMul(n):
    m = 1
    while n > 0:
        m *= n % 10
        n //= 10
    return m
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key = lambda x: (calMul(x), x))
    for i in a:
        print(i, end=" ")
    print()

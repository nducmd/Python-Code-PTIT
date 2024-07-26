t = int(input())
while t > 0:
    t -= 1
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    M = max(a)
    for i in range(n):
        if a[i] == M:
            a = a[:i] + [m] + a[i:]
            break
    for i in range(n+1):
        if a[i] < 0:
            print(a[i], end = " ")
    for i in range(n+1):
        if not (a[i] < 0):
            print(a[i], end = " ")
    print()
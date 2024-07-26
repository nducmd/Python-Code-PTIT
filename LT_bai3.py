isPrime = [0] * 1000005
for i in range(2, 1000000):
    if isPrime[i] == 0:
        for j in range(i*i, 1000000, i):
            isPrime[j] = 1
res = 0
n = int(input())
lst = list(map(int, input().split()))
for i in range(n):
    m = lst[i]
    p = m
    cntT = 0
    cntG = 0
    while m  > 0 and isPrime[m] == 1:
        cntT += 1
        m += 1
    m = p
    while m  > 0 and isPrime[m] == 1:
        cntG += 1
        m -= 1
    res = max(res, min(cntG, cntT))
print(res)
    
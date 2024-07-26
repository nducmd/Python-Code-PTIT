isPrime = [0] * 1000005
for i in range(2, 1000000):
    if isPrime[i] == 0:
        for j in range(i*i, 1000000, i):
            isPrime[j] = 1

n = int(input())
a = [int(x) for x in input().split()]
b = []
for i in range(len(a)):
    if isPrime[a[i]] == 0:
        b.append(a[i])
        a[i] = -1
b.sort()
for i in range(len(a)):
    if a[i] == -1:
        print(b[0], end = " ")
        b.pop(0)
    else:
        print(a[i], end = " ")
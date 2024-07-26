isPrime = [0] * 1000005
for i in range(2, 1000000):
    if isPrime[i] == 0:
        for j in range(i*i, 1000000, i):
            isPrime[j] = 1

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    for i in range(12, n):
        if isPrime[i] == 0:
            s = str(i)
            x = s[::-1]
            if s != x and isPrime[int(x)] == 0 and int(x) > i and int(x) < n:
                print(s, x, end = " ")
    print()
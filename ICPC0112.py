isPrime = [0] * 1000005
for i in range(2, 1000000):
    if isPrime[i] == 0:
        for j in range(i*i, 1000000, i):
            isPrime[j] = 1
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    cnt = 0
    for i in range(2, n-5):
        if isPrime[i] == 0:
            if isPrime[i+6] == 0 and (isPrime[i+2] == 0 or isPrime[i+4] == 0):
                cnt += 1
    print(cnt)
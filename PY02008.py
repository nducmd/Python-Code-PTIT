def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
    return True
inp = list(map(int, input().split()))
n = inp[0]
x = inp[1]
cnt = 0
print(x, end = " ")
i = 2
while cnt < n:
    while not isPrime(i):
        i += 1
    print(x + i, end = " ")
    x = x + i
    i += 1
    cnt += 1
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
    return True
inp = list(map(int, input().split()))
n = inp[0]
m = inp[1]
while n > 0:
    n -= 1
    a = list(map(int, input().split()))
    for i in a:
        print(1 if isPrime(i) else 0, end = " ")
    print()
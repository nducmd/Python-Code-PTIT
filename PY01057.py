def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def check(n):
    for i in range(0, len(n)):
        tmp = int(n[i])
        if isPrime(i) ^ isPrime(tmp) == 1:
            return False
    return True

t = int(input())
while t > 0:
    n = input()
    print("YES" if check(n) else "NO")
    t -= 1
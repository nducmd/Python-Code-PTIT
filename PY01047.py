def isPrime(n):
    m = int(n)
    if m < 2:
        return False
    for i in range(2, int(m**0.5) + 1):
        if m % i == 0:
            return False
    return True
t = int(input())
while t > 0:
    n = input()
    print("YES" if isPrime(n[-4:]) else "NO")
    t -= 1
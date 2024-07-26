def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
while t > 0:
    n = input()
    sum = 0
    for c in n:
        sum += int(c)
    print("YES" if isPrime(sum) else "NO")
    t -= 1
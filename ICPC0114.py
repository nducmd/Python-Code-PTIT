def isPrime(m):
    if m < 2:
        return False
    for i in range(2, int(m**0.5) + 1):
        if m % i == 0:
            return False
    return True

def check(n):
    m = int(n)
    if not isPrime(m):
        return False
    m = int(n[::-1])
    if not isPrime(m):
        return False
    sum = 0
    for c in n:
        if not isPrime(int(c)):
            return False
        sum += int(c)
    return isPrime(sum)

t = int(input())
while t > 0:
    t -= 1
    n = input()
    print("Yes" if check(n) else "No") 
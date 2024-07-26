import math
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2))+1):
        if (n % i == 0):
            return False
    return True

t = int(input())

while t > 0:
    n = int(input())
    k = 0
    for i in range (1, n):
        if (gcd(i, n) == 1):
            k += 1
    if isPrime(k):
        print("YES")
    else:
        print("NO")
    t -= 1

import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def check(str):
    tmp = sum(int(c) for c in str)
    if isPrime(tmp):
        print("YES")
    else:
        print("NO")

t = int(input())

while t > 0:
    inp = list(map(int, input().split()))
    a = inp[0]
    b = inp[1]
    c = math.gcd(a, b)
    check(str(c))
    t -= 1
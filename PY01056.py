def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def check(n):
    sum = 0
    for c in n:
        sum += int(c)
    for i in range(0, len(n), 2):
        if int(n[i]) & 1 == 1:
            return False
    for i in range(1, len(n), 2):
        if int(n[i]) & 1 == 0:
            return False
    return isPrime(sum)

t = int(input())
while t > 0:
    n = input()
    print("YES" if check(n) else "NO")
    t -= 1
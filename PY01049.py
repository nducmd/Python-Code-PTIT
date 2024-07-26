def isPrime(m):
    if m < 2:
        return False
    for i in range(2, int(m**0.5) + 1):
        if m % i == 0:
            return False
    return True
def check(n):
    if not isPrime(len(n)):
        return False
    cnt = 0
    for c in n:
        if isPrime(int(c)):
            cnt += 1
    return cnt > len(n) - cnt

t = int(input())
while t > 0:
    n = input()
    t -= 1
    print("YES" if check(n) else "NO")
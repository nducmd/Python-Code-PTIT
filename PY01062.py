def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
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
    print("YES" if check(n) else "NO")
    t -= 1
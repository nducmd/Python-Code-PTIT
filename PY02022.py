def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
dic = {}
for i in a:
    if isPrime(i):
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
for i in a:
    if i in dic and dic[i] > 0:
        print(i, dic[i])
        dic[i] = 0
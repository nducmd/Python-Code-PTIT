def calSum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key = lambda x: (calSum(x), x))
    for i in a:
        print(i, end=" ")
    print()

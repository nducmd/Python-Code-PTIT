def check(a, b):
    for i in range(len(a)):
        if (a[i] > b[i]):
            return False
    return True
n = int(input())
for _ in range(n):
    m = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a.sort()
    b.sort()
    print('YES' if check(a, b) else 'NO')
    
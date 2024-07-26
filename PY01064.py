l = [0]*30
l[0] = 0
l[1] = 1
l[2] = 3
for i in range(3, 28):
    l[i] = l[i-1] * 2 + 1

t = int(input())

while t > 0:
    t -= 1
    n, k = [int(x) for x in input().split()]
    while k != l[n-1] + 1:
        if k < l[n-1] + 1:
            n -= 1
        elif k > l[n-1] + 1:
            k -= l[n-1] + 1
    print(chr(ord('A') + n-1))

def check(n, base):
    res = ''
    while n > 0:
        res += str(n % base)
        n //= base
    return res == res[::-1]

a,b,m = [int(x) for x in input().split()]
res = [i for i in range(a, b+1) if check(i, 2)]
for i in range(3, m+1):
    res = [j for j in res if check(j,i)]
    if len(res) == 0:
        break
print(len(res))
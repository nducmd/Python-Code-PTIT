import math
def cnt(n):
    if n < 2:
        return 0
    else:
        return math.factorial(n) // (2 * math.factorial(n-2))
n = int(input())
h = [0] * n
c = [0] * n
for i in range(n):
    s = input()
    for j in range(len(s)):
        if s[j] == 'C':
            c[j] += 1
            h[i] += 1
res = 0
for i in range(n):
    res += cnt(h[i])
    res += cnt(c[i])
print(res)

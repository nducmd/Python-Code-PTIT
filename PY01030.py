import math
inp = input();
lst = list(inp.split())
n = int(lst[0])
k = int(lst[1])
m = 1
while k > 1:
    m = m * 10
    k -= 1
cnt = 0
for i in range(m, m*10):
    if math.gcd(i, n) == 1:
        print(i, end = " ")
        cnt += 1
    if cnt == 10:
        print()
        cnt = 0
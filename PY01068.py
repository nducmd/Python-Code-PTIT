from itertools import combinations
n, m = [int(x) for x in input().split()]
ms = set()
for i in input().split():
    ms.add(i)

a = list(ms)
a.sort()
combs = combinations(a, m)
b = []
for i in combs:
    b.append(" ".join(i))
b.sort()
print(*b, sep="\n")

# 6 2
# DONG TAY NAM BAC TAY BAC
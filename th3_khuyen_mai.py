class Product:
    def __init__(self, before, after, index):
        self.before = before
        self.after = after
        self.index = index
        self.profit = after - before
    def __lt__(self, other):
        return self.profit > other.profit
    def __str__(self):
        return str(self.index)
    
P = []
buy_before = set()
n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
for i in range(n):
    P.append(Product(a[i], b[i], i))
P.sort()
j = 0
for i in range(k):
    buy_before.add(int(str(P[j])))
    j += 1
    if j == n:
        break

res = 0
for i in range(n):
    if i in buy_before:
        res += a[i]
    else:
        res += min(b[i], a[i])
    
print(res)

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

k = int(input())
tren = 0
duoi = 0
for i in range(n):
    for j in range(n):
        if j > n - i -1:
            tren += a[i][j]
        elif j < n - i -1:
            duoi += a[i][j]

h = abs(tren - duoi)
print("YES" if h <= k else "NO")
print(h)
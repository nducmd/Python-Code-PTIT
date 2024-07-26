n = int(input())
a = [0] * (n+1)
for _ in range(n-1):
    x, y = [int(x) for x in input().split()]
    a[x] += 1
    a[y] += 1

cnt = 0
for i in range(1, n+1):
    if a[i] == 1:
        cnt += 1

print("Yes" if cnt == n-1 else "No")
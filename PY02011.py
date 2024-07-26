n = int(input())
lst = list(map(int, input().split()))
res = 99999999999
m = 0
p = 0
for i in range(n):
    p = lst[i]
    cnt = 0
    for j in range(n):
        if (p != lst[j]):
            cnt += abs(lst[j] - p)
    if (cnt < res):
        res = cnt
        m = p

print(res, m)
n = int(input())
a = [int(x) for x in input().split()]
a.append(-1)
res = 0
max_val = max(a)
cnt = 0
for i in a:
    if i == max_val:
        cnt += 1
    else:
        res = max(res, cnt)
        cnt = 0
        
print(res)

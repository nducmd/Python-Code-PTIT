n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
m = {}
for num in a:
    if num in m:
        m[num] += 1
    else:
        m[num] = 1
    
sorted_m = dict(sorted(m.items(), key = lambda x: (-x[1], x[0])))
b = list(sorted_m.items())
res = -1
if len(b) >= 2:
    n1 = b[0][1]
    for i in range(1, len(b)):
        if b[i][1] < n1:
            res = b[i][0]
            break

if res == -1:
    print("NONE")
else:
    print(res)
    

n = input()
K = int(input())
m = {}
if len(n) % 2 == 1:
    n = n[:-1]
for i in range(0,len(n)-1,2):
        curr = n[i] + n[i+1]
        if curr in m:
            m[curr] += 1
        else:
            m[curr] = 1
flag = 0
a = list(m.keys())
a.sort()
for item in a:
    if m[item] >= K:
        print(item, m[item])
        flag = 1
if flag == 0:
    print("NOT FOUND")
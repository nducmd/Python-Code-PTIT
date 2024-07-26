
n = int(input())
a = []
for i in range(n):
    a.append(input())
    
res = 0
h = [0] * n
c = [0] * n

for i in range(n):
    for j in range(n):
        if a[i][j] == 'C':
            h[i] += 1
            c[j] += 1
            
for i in range(n):
    for j in range(n):
        res += c[i] * (c[i] - 1) / 2
        res += h[i] * (h[i] - 1) / 2
print(int(res / n))



# 4
# CC..
# C..C
# .CC.
# .CC.
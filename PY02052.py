n = int(input())
a = []
for i in range(n):
    tmp = [int(x) for x in input().split()]
    a.append(tmp)
    
k = int(input())
s1 = 0
s2 = 0
for i in range(n):
    for j in range(n):
        if i != j:
            if i < j:
                s1 += a[i][j]
            else:
                s2 += a[i][j]
                
if abs(s1-s2) <= k:
    print("YES")
else:
    print("NO")
print(abs(s1-s2))

# 5
# 2 8 10 6 7
# 6 3 2 6 9
# 10 2 6 2 8
# 9 9 7 9 8
# 9 6 5 6 9
# 5
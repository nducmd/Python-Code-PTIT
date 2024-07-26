n, m = [int(x) for x in input().split()]
a = []
for i in range(n):
    tmp = [int(x) for x in input().split()]
    a.append(tmp)
deleted = []    
if n > m:
    k = 0
    for i in range(n-m):
        deleted.append(k)
        k += 2
    for i in range(n):
        if i not in deleted:
            for j in range(m):
                print(a[i][j], end = " ")
            print()
elif m > n:
    k = 1
    for i in range(m-n):
        deleted.append(k)
        k += 2
    for i in range(n):
            for j in range(m):
                if j not in deleted:
                    print(a[i][j], end = " ")
            print()
else:
    for i in range(n):
        for j in range(m):
            print(a[i][j], end = " ")
        print()
        
# 6 4
# 2 8 7 6
# 6 3 2 6
# 7 2 2 8
# 9 9 9 8
# 9 6 6 3
# 7 7 4 9

# 4 6
# 2 8 7 6 4 3
# 6 3 2 6 7 2
# 7 2 2 8 9 1
# 9 9 9 8 0 7
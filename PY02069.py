def check(s):
    return s == s[::-1] and len(s) >= 2

n,m = [int(x) for x in input().split()]
a = []
for i in range(n):
    row = [str(x) for x in input().split()]
    a.append(row)

MAX = 0
for i in range(n):
    for j in range(m):
        if check(a[i][j]) and int(a[i][j]) > MAX:
            MAX = int(a[i][j])
if MAX == 0:
    print("NOT FOUND")
else:
    print(MAX)
    for i in range(n):
        for j in range(m):
            if a[i][j] == str(MAX):
                print("Vi tri [" + str(i) + "][" + str(j) + "]") 


P = [0] * 1000005
P[0] = P[1] = 1
for i in range(2, 1000000):
    if P[i] == 0:
        for j in range(i*i, 1000000, i):
            P[j] = 1
            
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n,m = [int(x) for x in input().split()]
a = []
for i in range(n):
    tmp = [int(x) for x in input().split()]
    a.append(tmp)
    
max_val = -1
for i in range(n):
    for j in range(m):
        if P[a[i][j]] == 0:
            max_val = max(max_val, a[i][j])
if max_val == -1:
    print("NOT FOUND")
else:
    print(max_val)
    for i in range(n):
        for j in range(m):
            if a[i][j] == max_val:
                vt = "[" + str(i) + "][" + str(j) + "]" 
                print("Vi tri " + vt)
            

            
# 6 4
# 23 21 26 10
# 13 13 22 14
# 28 29 28 23
# 29 19 11 19
# 16 26 24 21
# 13 25 21 29
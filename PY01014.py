a, k, n = [int(x) for x in input().split()]

start = (k - (a % k)) % k
flag = 0
while a + start <= n:
    if start > 0:
        print(start, end = " ")
        flag = 1
    start += k
    
if flag == 0:
    print("-1")
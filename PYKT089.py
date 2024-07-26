n = int(input())
a = []
while len(a) < n:
    a += [int(x) for x in input().split()]

b = [x for x in a if x % 2 == 1]
b.sort()
b = b[::-1]
c = [x for x in a if x % 2 == 0]
c.sort()
j = 0
k = 0
for i in range(len(a)):
    
    if a[i] % 2 != 0:
        print(b[j], end = " ")
        j += 1
    else:
        print(c[k], end = " ")
        k += 1
n,m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
A = set(a)
B = set(b)
c = list(A.intersection(B))
d = list(A - B)
e = list(B - A)
c.sort()
d.sort()
e.sort() 
for i in c:
    print(i, end = " ")
print()
for i in d:
    print(i, end = " ")
print()
for i in e:
    print(i, end = " ")
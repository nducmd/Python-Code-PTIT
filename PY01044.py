x1 = input().lower()
x2 = input().lower()
a = set(x1.split())
b = set(x2.split())
d = sorted(a.union(b))
c = sorted(a.intersection(b))
for i in d:
    print(i, end = " ")
print()
for i in c:
    print(i, end = " ")

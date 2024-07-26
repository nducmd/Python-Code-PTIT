a = []
while len(a) < 10:
    a += list(map(int, input().split()))

for i in range(10):
    a[i] = a[i] % 42

b = set(a)
print(len(b))
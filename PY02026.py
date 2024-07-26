def check(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if (a[i] != b[i]):
            return False
    return True
n,m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
A = set(a)
B = set(b)
c = list(A)
d = list(B)
print("YES" if check(c, d) else "NO")
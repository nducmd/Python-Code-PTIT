n,m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = set(a)
d = set(b)
print("YES" if c == d else "NO")
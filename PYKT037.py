def con(n):
    if n < 10:
        return str(n)
    return chr(n+55)
def to_base(n, b):
    s = ""
    while n > 0:
        s += con(n % b)
        n //= b
    return s[::-1]

n = int(input())
for _ in range(n):
    a,b = [int(x) for x in input().split()]
    print(to_base(a,b))
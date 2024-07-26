def to_base(n, b):
    s = ""
    while n > 0:
        s += str(n % b)
        n //= b
    return s

s = input()
while len(s) % 3 != 0:
    s = '0' + s

x = ""
tmp = ""
for c in s:
    tmp += c
    if len(tmp) == 3:
        x += str(int(tmp,2))
        tmp = ""
print(x)
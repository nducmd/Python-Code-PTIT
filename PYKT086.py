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
with open('DATA.in') as f:
    
    t = int(f.readline().strip())
    while t > 0:
        t -= 1
        b = int(f.readline().strip())
        s = f.readline().strip()

        s = s[::-1]
        x = 0
        for i in range(len(s)):
            x += 2**i * int(s[i])
        print(to_base(x, b))
    
# 2
# 8
# 10010100010010101
# 2
# 10010100010010101
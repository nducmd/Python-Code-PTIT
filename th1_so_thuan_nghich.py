def check(n, b):
    s = ""
    while n > 0:
        s += str(n % b)
        n //= b
    return s == s[::-1]

def check_b2(n):
    s = bin(n)[2:]
    return s == s[::-1]
    
a,b,m = [int(x) for x in input().split()]
lst = [i for i in range(a, b+1) if check_b2(i)]

for i in range(3, m+1):
    lst = [j for j in lst if check(j,i)]

print(len(lst))
def ucln(a, b):
    r = a % b
    while b != 0:
        r = a % b
        a = b
        b = r  
    return a

t = int(input())
while t > 0:
    t -= 1
    a, b = [int(x) for x in input().split()]
    print(ucln(a, b))
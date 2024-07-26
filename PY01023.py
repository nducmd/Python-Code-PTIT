import math
def factor(n):
    print(1, end = "")
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            cnt = 0
            while (n % i == 0):
                cnt += 1
                n //= i
            print(" *", end = " ")
            print(str(i) + "^" + str(cnt), end = '')
    if n > 1:
        print(" *", end = " ")
        print(str(n) + "^" + str(1), end = "")
    print()
t = int(input())
while t > 0:
    n = int(input())
    factor(n)
    t -= 1
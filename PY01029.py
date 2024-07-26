import math
t = int(input())
while t > 0:
    t -= 1
    n = input()
    m = n[::-1]
    print("YES" if math.gcd(int(n), int(m)) == 1 else "NO")
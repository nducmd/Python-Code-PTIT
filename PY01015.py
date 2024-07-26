def check(str):
    m = 0
    for c in str:
        if int(c) < m:
            return False
        else:
            m = int(c)
    return True

t = int(input())
while t > 0:
    str = input()
    print("YES" if check(str) else "NO")
    t -= 1

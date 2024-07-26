def check(n):
    for c in n:
        if c != '0' and c != '1' and c != '2':
            return False
    return True
t = int(input())
while t > 0:
    print("YES" if check(input()) else "NO")
    t -= 1
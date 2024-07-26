def check(n):
    if n[0] == n[1]:
        return False
    for i in range(2, len(n)):
        if n[i] != n[i & 1]:
            return False
    return True

t = int(input())
while t > 0:
    t -= 1
    print("YES" if check(input()) else "NO")
def check(s):
    return s[0] == s[-1]
t = int(input())
while t > 0:
    t -= 1
    s = input()
    print("YES" if check(s) else "NO")
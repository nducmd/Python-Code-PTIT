def check(s):
    x = s[::-1]
    for i in range(0, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(x[i]) - ord(x[i-1])):
            return False
    return True
t = int(input())
while t > 0:
    t -= 1
    s = input()
    print("YES" if check(s) else "NO")

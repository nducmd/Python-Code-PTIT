t = int(input())
while t > 0:
    n = input()
    sum = 0
    for c in n:
        sum += int(c)
    print("YES" if sum % 3 == 0 else "NO")
    t -= 1
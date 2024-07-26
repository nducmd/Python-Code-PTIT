t = int(input())
while t > 0:
    n = input()
    sum = 0
    for c in n:
        sum += int(c)
    j = str(sum)
    jj = j[::-1]
    print("YES" if j == jj and len(j) > 1 else "NO")
    t -= 1
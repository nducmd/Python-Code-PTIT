t = int(input())
while t > 0:
    n = input()
    sum = 1
    for c in n:
        if c != '0':
            sum *= int(c)
    print(sum)
    t -= 1
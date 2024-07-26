def bankRate(a, b, c):
    year = 0
    while (a < c):
        year += 1
        interest = (a / 100.0) * b
        a = a + interest
    return year

t = int(input())
while t > 0:
    inp = list(map(float, input().split()))
    print(bankRate(inp[0], inp[1], inp[2]))
    t -= 1
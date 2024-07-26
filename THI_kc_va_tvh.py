t = int(input())
while t > 0:
    t -= 1
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    d = 0.0
    tvh = 0
    for i in range(len(a)):
        d += (a[i] - b[i]) * (a[i] - b[i])
        tvh += a[i] * b[i]
    print("{:.2f}".format(d**0.5) + " " + str(tvh))
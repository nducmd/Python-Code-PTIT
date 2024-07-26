def count(x, digit):
    power = 1
    cnt = 0
    left = x
    right = 0

    while left > 0:
        current = left % 10
        left //= 10
        cnt += left * power
        if current == digit:
            cnt += right + 1
        elif current > digit:
            cnt += power
        power *= 10
        right = x % power

    if digit == 0:
        cnt -= (power - 1) // 9

    return cnt


t = int(input())
while t > 0:
    t -= 1
    a, b = [int(x) for x in input().split()]

    res = [0] * 10

    for digit in range(10):
        res[digit] = count(b, digit)
        if a - 1 > 0:
            res[digit] -= count(a - 1, digit)

    print(*res)

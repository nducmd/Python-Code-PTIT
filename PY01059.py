def cal(n):
    sum = 0
    mul = 1
    flag = 0
    for i in range(0, len(n), 2):
        sum += int(n[i])
    for i in range(1, len(n), 2):
        if n[i] != '0':
            flag = 1
            mul *= int(n[i])
    print(sum, end = " ")
    if flag == 0:
        print(0)
    else:
        print(mul)

t = int(input())
while t > 0:
    n = input()
    cal(n)
    t -= 1
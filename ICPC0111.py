t = int(input())
while t > 0:
    t -= 1
    inp = list(map(int, input().split()))
    n = inp[0]
    k = inp[1]
    lst = list(map(int, input().split()))
    for i in range(k, n):
        print(lst[i], end = " ")
    for i in range(0, k):
        print(lst[i], end = " ")
    print()
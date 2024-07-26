t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    cnt = 0
    for i in range(n-2):
        j = i + 1
        k = n - 1
        while j < k:
            if lst[i] + lst[j] + lst[k] < 0:
                j += 1
            elif lst[i] + lst[j] + lst[k] > 0:
                k -= 1
            else:
                j += 1
                cnt += 1
    print(cnt)

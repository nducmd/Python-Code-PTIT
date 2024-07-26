t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    dic = {}
    for item in a:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] += 1
    m = max(dic.values())
    res = 9999999999999
    for key, val in dic.items():
        if val == m:
            res = min(key, res)
    print(res if m > (n/2) else "NO")
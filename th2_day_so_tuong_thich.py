def check(a, k):
    b = []
    for i in range(len(a)):
        p = a[i] // k
        j = 0
        while (p-j) != 0 and a[i] // (p-j) == k :
            j += 1
        j -= 1
        if (a[i] // (p-j) == k):
            b.append(p-j)
        else:
            return -1
    # print(k, b)
    return sum(b)
    
n = int(input())
a = [int(x) for x in input().split()]
s = min(a)
for i in range(s, 0, -1):
    res = check(a,i)
    if res != -1:
        print(res)
        break
    
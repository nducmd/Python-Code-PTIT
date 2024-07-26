l = []
l.append(0)
l.append(1)
l.append(3)
def cntLength() :
    for i in range(3, 27):
        l.append(l[-1] * 2 + 1)
cntLength()
t = int(input())
while t > 0:
    t -= 1
    lst = list(map(int, input().split()))
    n = lst[0]
    k = lst[1]
    while k != l[n-1] + 1:
        if k < l[n-1] + 1:
            n -= 1
        elif k > l[n-1] + 1:
            k -= l[n-1] + 1
    print(chr(ord('A') + n -1))

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [int(x) for x in input().split()]
    m = {}
    for i in a:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    for k,v in m.items():
        if v % 2 == 1:
            print(k)
            break
        
# 2
# 7
# 1 2 3 2 3 1 3
# 5
# 1 1 3 3 2
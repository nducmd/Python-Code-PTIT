
res = []
def Try(N, max_val, curr =[]):
    if N == 0:
        tmp = "("
        for j in curr:
            tmp = tmp + str(j) + " "
        tmp = tmp[0:-1]
        tmp += ")"
        res.append(tmp)
    
    for i in range(min(N, max_val), 0, -1):
        curr.append(i)
        Try(N-i, i, curr)
        curr.pop()
        

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    res.clear()
    Try(n, n)
    print(len(res))
    for s in res:
        print(s, end = " ")
    print()
    
    
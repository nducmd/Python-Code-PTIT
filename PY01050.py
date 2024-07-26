def check(n):
    if not( 'A' in n and 'B' in n and 'C' in n):
        return False
    cntA = 0
    cntB = 0
    cntC = 0
    for c in n:
        if c == 'A':
            cntA += 1
        elif c == 'B':
            cntB += 1
        else:
            cntC += 1
    if cntA <= cntB and cntB <= cntC:
        return True
    return False
n = int(input())
lst = []
lst.append("A")
lst.append("B")
lst.append("C")
for item in lst:
    if len(item) > n-1:
        break
    tmp = item + 'A'
    if check(tmp):
        print(tmp)
    lst.append(tmp)
    tmp = item + 'B'
    if check(tmp):
        print(tmp)
    lst.append(tmp)
    tmp = item + 'C'
    if check(tmp):
        print(tmp)
    lst.append(tmp)


def check(n):
    for c in n:
        if int(c) & 1:
            return False
    return True
def create():
    lst = []
    for i in range(2,10000,2):
        j = str(i)
        if check(j):
            j = j[::-1]
            tmp = int(str(i) + j)
            lst.append(tmp)
    return lst
lst =[]
lst = create()
t = int(input())
while t > 0:
    n = int(input())
    for item in lst:
        if item >= n:
            break
        else:
            print(item, end = " ")
    print()
    t -= 1
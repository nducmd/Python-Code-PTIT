def check(str):
    if '1' in str or '3' in str or '5' in str or '7' in str or '9' in str:
        return False
    return True

t = int(input())

lst = []

num = 2

while num <= 888:
    if check(str(num)):
        tmp = str(num)
        lst.append(int(tmp + tmp[::-1]))
    num += 2

while t > 0:
    n = int(input())
    for item in lst:
        if item < n:
            print(item, end = " ")
    print()
    t -= 1
n = input()
while len(n) > 1:
    a = n[0:len(n)//2]
    b = n[len(n)//2:]
    tmp = int(a) + int(b)
    print(tmp)
    n = str(tmp)
    
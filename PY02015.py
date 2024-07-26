while True:
    inp = input()
    if inp == "0 0 0 0":
        break
    a = list(map(int, inp.split()))
    cnt = 0
    while len(set(a)) != 1:
        tmp = a[0]
        a[0] = abs(a[0] - a[1])
        a[1] = abs(a[1] - a[2])
        a[2] = abs(a[2] - a[3])
        a[3] = abs(a[3] - tmp)
        cnt += 1
    print(cnt)
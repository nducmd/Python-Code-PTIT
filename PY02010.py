
while True:
    n = int(input())
    if n == 0:
        break
    a = []
    for i in range(n):
        a.append(int(input()))
    m = a[0]
    M = a[0]
    for i in range(n):
        if a[i] > M:
            M = a[i]
        if a[i] < m:
            m = a[i]
    if m == M:
        print("BANG NHAU")
    else:
        print(m, M)
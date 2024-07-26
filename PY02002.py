f = [0] * 94
f[0] = 1
f[1] = 1
f[2] = 1
for i in range(3, 93):
    f[i] = f[i-1] + f[i-2]
t = int(input())
while t > 0:
    t -= 1
    inp = list(map(int, input().split()))
    a = inp[0]
    b = inp[1]
    for i in range(a,b+1):
        print(f[i] , end = " ")

    print()
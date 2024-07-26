inp = list(map(int,input().split()))
n = inp[0]
k = inp[1]
lst = list(map(int,input().split()))
a = []
for item in lst:
    if item not in a:
        a.append(item)
a.sort()
b = []
for i in range(0, k+1):
    b.append(i)

while True:
    for i in range(1, k+1):
        print(a[b[i]-1], end = " ")
    print()
    i = k
    while i > 0 and b[i] >= len(a) -k +i:
        i -= 1
    if i == 0:
        break
    b[i] += 1
    for j in range(i+1, k+1):
        b[j] = b[i] + j - i
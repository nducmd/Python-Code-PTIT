n = int(input())
a = [int(x) for x in input().split()]
a.sort()
x1 = a[0] * a[1]
x2 = a[0] * a[1] * a[-1]
x3 = a[-1] * a[-2] * a[-3]
x4 = a[-1] * a[-2]
print(max(x1,x2,x3,x4))
def euclid(a, b):
    d = 0
    for i in range(len(a)):
        d += (a[i] - b[i]) * (a[i] - b[i])
    return d ** 0.5
def manha(a, b):
    d = 0
    for i in range(len(a)):
        d += abs(a[i] - b[i])
    return d
def mink(a, b, p):
    d = 0
    for i in range(len(a)):
        d += (abs(a[i] - b[i]) ** p)
    return d ** (1/p)
def jaccard(x, y):
    a = set(x)
    b = set(y)
    d = len(a.intersection(b)) / len(a.union(b))
    return d 

t = int(input())

while t > 0:
    t -= 1
    s = input()
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    if len(a) != len(b):
        print("Invalid")
    else:
        if s == "euclidean":
            print("{:.5f}".format(euclid(a, b)))
        elif s == "manhattan":
            print("{:.5f}".format(manha(a, b)))
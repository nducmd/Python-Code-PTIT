import math
lst = list(map(int, input().split()))
a = lst[0]
b = lst[1]
for i in range(a, b+1):
    for j in range(i+1, b+1):
        for k  in range(j+1, b+1):
            if math.gcd(i,j) == 1 and math.gcd(j,k) == 1 and math.gcd(i, k) == 1:
                print("(", end="")
                print(i, end = ", ")
                print(j, end = ", ")
                print(k, end = ")")
                print()
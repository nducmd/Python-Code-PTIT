from itertools import permutations

t = int(input())
while t > 0:
    t -= 1
    s = ""
    n = int(input())
    for i in range(1, n+1):
        s += str(i)
    perms = list(reversed(list(permutations(s))))
    print(len(perms))
    for i in perms:
        print("".join(i), end = " ")
    print()
    
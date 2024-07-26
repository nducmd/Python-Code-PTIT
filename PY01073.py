from itertools import permutations
s = input()
a = set()
perms = permutations(s)
for i in perms:
    print("".join(i))
    
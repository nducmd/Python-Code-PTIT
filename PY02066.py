a = []
n = int(input())
while len(a) < n:
    tmp = [int(x) for x in input().split()]
    a += tmp
flag = 0
for i in range(1, max(a)+1):
    if i not in a:
        flag = 1
        print(i)
if flag == 0:
    print("Excellent!")
    
# 7
# 4 5 7 8 9
# 10 11
# 5
# 1 2 3
# 4
# 5

# 4
# 1 2 3 5
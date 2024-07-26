from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**6)
t = int(input())
tmp_names = set()
a = []
while t > 0:
    t -= 1
    n1, s, n2 = input().split()
    tmp_names.add(n1)
    tmp_names.add(n2)
    if s == '>':
        a.append((n1, n2))
    else:
        a.append((n2, n1))
names = list(tmp_names)
m = {}
idx = 0
for i in names:
    m[i] = idx
    idx += 1
    
n = idx

ke = [[] for _ in range(n)]
for n1, n2 in a:
    ke[m[n1]].append(m[n2])

color = [0] * n 

def dfs(i):
    color[i] = 1
    for j in ke[i]:
        if color[j] == 0:
            if dfs(j):
                return True
        if color[j] == 1:
            return True
    color[i] = 2
    return False

flag = 0
for i in range(n):
    if color[i] == 0:
        if (dfs(i)):
            flag = 1
            break
        
print("impossible" if flag == 1 else "possible")
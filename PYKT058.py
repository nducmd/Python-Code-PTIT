ke = []
def bfs(n, k, u, v):
    q = [u]
    visited = [0] * (n+1)
    visited[u] = 1
    while len(q) > 0:
        top = q[0]
        q.pop(0)
        if top == v:
            return False
        for i in ke[top]:
            if visited[i] == 0 and i != k:
                q.append(i)
                visited[i] = 1
    return True
t = int(input())
while t > 0:
    t -= 1
    n, m, u, v = [int(x) for x in input().split()]
    ke.clear()
    for i in range(n+1):
        ke.append([])
    
    for i in range(m):
        x, y = [int(z) for z in input().split()]
        ke[x].append(y) 
    
    res = 0
    for i in range(1, n+1):
        if i != u and i != v:
            if bfs(n, i, u, v):
                res += 1
    print(res)   
    
# 2
# 5 7 1 3
# 1 2
# 2 4
# 2 5
# 3 1
# 3 2
# 4 3
# 5 4
# 4 5 1 4
# 1 2
# 1 3
# 2 3
# 2 4
# 3 4
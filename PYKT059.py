n, m, k = [int(x) for x in input().split()]
ke = []
for i in range(n+1):
    ke.append([])
    
for _ in range(m):
    x, y = [int(x) for x in input().split()]
    ke[x].append(y)
    ke[y].append(x)

st = []
visited = [0] * (n+1)
visited[k] = 1
st.append(k)
while len(st) > 0:
    top = st[-1]
    st.pop()
    for i in ke[top]:
        if visited[i] == 0:
            visited[i] = 1
            st.append(top)
            st.append(i)
            break

for i in range(1, n+1):
    if visited[i] == 0:
        print(i)
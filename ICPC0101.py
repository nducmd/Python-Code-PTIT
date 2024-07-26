n = int(input())
lst = list(map(int, input().split()))
st = []
for i in range(n):
    m = lst[i]
    if len(st) != 0:
        p = st.pop()
        if (m + p) & 1 == 1:
            st.append(p)
            st.append(m)
    else:
        st.append(m)

print(len(st))
n = int(input())
lst = list(map(int, input().split()))
st = []
cnt = 0
for i in range(n):
    if len(st) != 0:
        p = st.pop() 
        if p != lst[i]:
            cnt += 1
            st.append(p)
            st.append(lst[i])
        else:
            st.append(p)
    else:
        st.append(lst[i])
print(cnt)
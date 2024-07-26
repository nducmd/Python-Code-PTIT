class Item:
    def __init__(self, val, behind, same):
        self.val = val
        self.behind = behind
        self.same = same


n = int(input())
st = []
res = 0

for i in range(n):
    h = int(input())
    if len(st)!= 0:
        top = st[-1]
    if len(st) == 0:
        st.append(Item(h, 0, 0))
    elif top and top.val > h:
        st.append(Item(h, 1, 0))
        res += 1
    elif top and top.val == h:
        res += 1
        res += top.same
        if top.behind == 1:
            res += 1
        st.append(Item(h, top.behind, top.same + 1))
    elif top and top.val < h:
        while len(st)!=0 and st[-1].val < h:
            res += 1
            st.pop()
        if len(st) != 0:
            top = st[-1]
        if top and top.val == h:
            res += 1
            res += top.same
            if top.behind == 1:
                res += 1
            st.append(Item(h, top.behind, top.same + 1))
        elif top and top.val > h:
            res += 1
            st.append(Item(h, 1, 0))
        else:
            st.append(Item(h, 0, 0))

print(res)

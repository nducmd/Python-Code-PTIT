t = int(input())
while t > 0:
    t -= 1
    s = input()
    st = []
    k = 1
    res = []
    for i in range(len(s)):
        if s[i] == '(':
            st.append(k)
            res.append(k)
            k += 1
        elif s[i] == ')':
            res.append(st[-1])
            st.pop()
            
    for i in res:
        print(i, end = " ")
    print()
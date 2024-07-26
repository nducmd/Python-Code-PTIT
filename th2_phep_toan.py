flag = 0
sign = '+-*'
n,m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
si = []
curr = []
tmp = []
def cnt(cu):
    st = []
    j = 0
    st.append(a[j])
    j += 1
    for i in range(len(cu)):
        if cu[i] == '+' or cu[i] == '-':
            st.append(cu[i])
            st.append(a[j])
            j += 1
        else:
            tmp = st[-1]
            st.pop()
            tmp = tmp * a[j]
            j += 1
            st.append(tmp)
    sum = st[0]
    for i in range(len(st)):
        if st[i] == '+':
            sum += st[i+1]
        elif st[i] == '-':
            sum -= st[i+1]
    # print(st, sum)
    if sum == m:
        global flag
        flag = 1
        cu.append('=')
        for i in range(n):
            if (a[i] < 0):
                tmp = '(' + str(a[i]) + ')'
                print(tmp, end = "")
            else:
                print(a[i], end = "")
            print(cu[i], end = "")
        print(m)
def Try(i, n):
    if i == n - 1:
        curr = []
        for j in range(n-1):
            curr.append(si[j])
        cnt(curr)
        # print(curr)
        return
    else:
        for c in sign:
            si.append(c)
            Try(i+1, n)
            si.pop()
Try(0, n)        
if flag == 0:
    print("IMPOSSIBLE")
# print(a)

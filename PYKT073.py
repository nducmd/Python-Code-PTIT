n = int(input())
a = []
for _ in range(n):
    a.append(len(input().split()))


st = []
res = []
for i in range(n):
    if a[i] == 6 or a[i] == 8:
        if len(st) == 0 or st[-1] == 6 or st[-1] == 8:
            st.append(a[i])
        else:
            res.append(st[-1])
            st.clear()
            st.append(a[i])
    else:
        if len(st) == 0 or (st[-1] == 7 and len(st) < 4):
            st.append(a[i])
        else:
            res.append(st[-1])
            st.clear()
            st.append(a[i])
res.append(st[-1])
print(len(res))
for i in range(len(res)):
    print(res[i] % 2 + 1)
            
            

# 12
# Minh ve minh co nho ta
# Muoi lam nam ay thiet tha man nong
# Minh ve minh co nho khong
# Nhin cay nho nui nhin song nho nguon
# Mot canh hai canh lai ba canh
# Tran troc ban khoan giac chang lanh
# Canh bon canh nam vua chop mat
# Sao vang nam canh mong hon bay
# Mot canh hai canh lai ba canh
# Tran troc ban khoan giac chang lanh
# Canh bon canh nam vua chop mat
# Sao vang nam canh mong hon bay
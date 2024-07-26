import re
t = int(input())
a = []
while t > 0:
    t -= 1
    b = re.split("[^a-z0-9]", input().lower())
    a += b
m = {}
for i in a:
    if i != '':
        if i in m:
            m[i] += 1
        else:
            m[i] = 1

ms = dict(sorted(m.items(), key = lambda x : (-x[1], x[0])))
for k, v in ms.items():
    print(k, v)
# 3
# PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
# Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
# voi muc ho tro 500000 dong/sinh vien PTIT.
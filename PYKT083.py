def unit_price(vehicle, seat):
    if vehicle == 'Xe_con':
        if seat == '5':
            return 10000
        else:
            return 15000
    elif vehicle == 'Xe_tai':
        return 20000
    else:
        if seat == '29':
            return 50000
        else:
            return 70000
        

n = int(input())
m = {}
for _ in range(n):
    s = input().split()
    if s[3] == 'IN':
        
        if s[4] in m:
            m[s[4]] += unit_price(s[1], s[2])
        else:
            m[s[4]] = unit_price(s[1], s[2])

for k, v in m.items():
    print(k, end = ': ')
    print(v)
    
# 5
# 30F-123.15 Xe_con 5 OUT 06/11/2021
# 30F-123.15 Xe_con 5 IN 06/11/2021
# 30H-123.15 Xe_con 7 IN 06/11/2021
# 29H-222.68 Xe_tai 2 IN 07/11/2021
# 30G-511.15 Xe_con 5 IN 07/11/2021
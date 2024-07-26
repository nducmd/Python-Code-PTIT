def con(x):
    if x >=3 and x <=4 : return 2.5
    if x >=5 and x <=6 : return 3.0
    if x >=7 and x <=9 : return 3.5
    if x >=10 and x <=12 : return 4.0
    if x >=13 and x <=15 : return 4.5
    if x >=16 and x <=19 : return 5.0
    if x >=20 and x <=22 : return 5.5
    if x >=23 and x <=26 : return 6.0
    if x >=27 and x <=29 : return 6.5
    if x >=30 and x <=32 : return 7.0
    if x >=33 and x <=34 : return 7.5
    if x >=35 and x <=36 : return 8.0
    if x >=37 and x <=38 : return 8.5
    if x >=39 and x <=40 : return 9.0

t = int(input())
while t > 0:
    t -= 1
    inp = input().split()
    r = con(int(inp[0]))
    l = con(int(inp[1]))
    s = float(inp[2])
    w = float(inp[3])
    o = (r + l + s + w) / 4.0
    if o - int(o) >= 0.75:
        o = int(o) + 1.0
    elif o - int(o) >= 0.25:
        o = int(o) + 0.5
    else:
        o = o - (o - int(o))
    print(o)
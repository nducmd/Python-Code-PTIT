s = input()
myset = []
if len(s) % 2 == 1:
    s = s[:-1]
while len(s) > 0:
    tmp = s[0:2]
    s = s[2:]
    if tmp not in myset:
        myset.append(tmp)

for item in myset:
    print(item, end = " ")
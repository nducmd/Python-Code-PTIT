str = input()

cntLower = 0
cntUpper = 0
for i in range(0, len(str)):
    if str[i].islower():
        cntLower += 1
    else:
        cntUpper += 1
if cntLower >= cntUpper:
    print(str.lower())
else:
    print(str.upper())
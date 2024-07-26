s = input()
x = s[::-1]
cnt = 0
res = ""
for c in x:
    if cnt == 3:
        res += ","
        cnt = 0
    res += c
    cnt += 1
print(res[::-1])
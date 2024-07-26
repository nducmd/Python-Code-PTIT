def cntSum(s):
    n = 0
    for i in s : n += ord(i) - ord('0')
    return str(n)
n = input()
cnt = 0
while len(n) > 1:
    n = cntSum(n)
    cnt += 1
print(cnt)
s = input()
a = [0] * len(s)

for i in range(len(s)-2):
    if a[i] == 0 and s[i:i+3] == '688':
        a[i] = 1
        a[i+1] = 1
        a[i+2] = 1
        
for i in range(len(s)-1):
    if a[i] == 0 and s[i:i+2] == '68':
        a[i] = 1
        a[i+1] = 1
        
for i in range(len(s)):
    if a[i] == 0 and s[i] == '6':
        a[i] = 1
# print(a)  
print('YES' if not 0 in a else 'NO')
n = int(input())
a = ['2', '3', '5', '7']
res = set()
def check(s):
    if s[-1] == '2':
        return False
    for i in a:
        if i not in s:
            return False
    return True
def Try(s):
    if len(s) >= 4 and check(s):
        res.add(s)
    if len(s) == n:
        return
    for i in a:
        Try(s + i)
        
Try("")
for i in sorted(res, key= lambda x : int(x)):
    print(i)
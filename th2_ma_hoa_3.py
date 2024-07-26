def cntSum(s):
    sum = 0
    for c in s:
        sum += ord(c) - ord('A')
    return sum
def rotate(s, pad):
    pad = pad % 26
    x = ""
    for c in s:
        i = 0
        tmp = c
        while i < pad:
            if (tmp =='Z'):
                tmp = 'A'
            else:
                tmp = chr(ord(tmp) + 1)
            
            #print(tmp)    
            i += 1
        x += tmp
    return x
            
def encode(s):
    a = s[:(len(s)//2)]
    b = s[len(s)//2:]
    # print(a,cntSum(a), b, cntSum(b))
    # print(rotate(a, cntSum(a)), rotate(b, cntSum(b)))
    a = rotate(a, cntSum(a))
    b = rotate(b, cntSum(b))
    res = ""
    for i in range(len(a)):
        res += rotate(a[i], ord(b[i]) - ord('A'))
    print(res)
t = int(input())
while t > 0:
    t -= 1
    encode(input())
    
# 3
# EWPGAJRB
# BB
# TPQJDRJWSQXGRRIPXFMINTELHBJA
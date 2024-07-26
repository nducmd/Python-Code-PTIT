F = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

def encode(s, k):
    res = ""
    for c in s:
        i = F.index(c)
        res = res + F[(i+k) % 28]
    res = res[::-1]
    print(res)
inp = input()
while inp != "0":
    lst = list(inp.split())
    encode(lst[1], int(lst[0]))
    inp = input()

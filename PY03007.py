import re

inp = ""

while True:
    try:
        inp += input().lower()
    except:
        break

s = " ".join(inp.split())

res = re.split("[.?!]+", s)
for i in res:
    print(i.strip().capitalize())
#print(" ".join(inp.split()))

# ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010.... nhu vay, nam nay la          tron 10 nam!
#     vay CO PHAI NAM NAY LA KY THI LAN THU 10?        khong phai! nam nay la KY THI LAN THU 11.
n = int(input())

for _ in range(n):
    inp = input().split()
    i = 0
    res = ""
    while i < len(inp) and len(res) + len(inp[i]) < 100:
        res += inp[i] + " "
        #print(len(res))
        i += 1
    print(res)
    

# 2
# Can cu Ke hoach giang day – hoc tap hoc ky 1 nam hoc 2021 – 2022 Can cu ket qua thi hoc ky 2 va hoc ky phu ky he nam hoc 2020 – 2021
# Hoc vien Cong nghe Buu chinh Vien thong to chuc khai giang truc tuyen
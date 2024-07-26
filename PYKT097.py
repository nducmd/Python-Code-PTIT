inp = ""
while True:
    try:
        inp += input() + " * "
    except:
        break
a = inp.lower().split()

is_start = 1

for i in a:
    if i == "." or i == "?" or i == "!":
        print(i)
        is_start = 1
    elif "." in i or "?" in i or "!" in i:
        print(" ", end="")
        for j in i:
            if j in ".?!":
                print(j)
                is_start = 1
            else:
                if is_start == 1:
                    j = j.upper()
                    is_start = 0
                print(j, end = "")
    else:
        if is_start == 1:
            if i != "*":
                i = i.title()
                is_start = 0
                print(i, end = "")
        else:
            if i == "*":
                print(".")
                is_start = 1
            else:
                print(" ", end="")
                print(i, end = "")


# Chuong trinh Dao Tao CLC nganh CNTT duoc.Thiet     Ke theo chuan quoc te.
# co 03 chuyen nganh la: Cong  nghe phan mem, Tri tue nhan tao va An toan thong tin
# muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep
# moi    CAC BAN danG ky     thaM giA !
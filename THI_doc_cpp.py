
import re
import os

# Tên tệp CPP bạn muốn đọc
ten_tep_cpp = 'CHELLO.cpp'

# Đọc nội dung của tệp CPP
with open(ten_tep_cpp, 'r') as file:
    noi_dung = file.read()

# Sử dụng biểu thức chính quy để tìm tất cả các biến int
matches = re.findall(r'\bint\s+(\w+)\s*(?:\[\s*\d*\s*\])?\s*;', noi_dung)
print(*matches)
# Tính toán tổng số byte được sử dụng cho biến int
kich_thuoc_int = 4  # Giả sử biến int chiếm 4 byte
tong_so_byte = len(matches) * kich_thuoc_int

print(f"Tổng số byte được sử dụng cho biến int là: {tong_so_byte} byte")

import struct

with open("SONGUYEN.in", 'rb') as file:
    # Đọc lần lượt từng 4 byte
    while True:
        binary_data = file.read(4)
        
        # Kiểm tra xem có đủ byte để chuyển đổi thành số nguyên không
        if len(binary_data) == 0:
            break  # Kết thúc nếu không còn dữ liệu
        elif len(binary_data) < 4:
            print(f"Không đủ byte ({len(binary_data)}) để chuyển đổi thành số nguyên.")
        else:
            # Chuyển đổi từng 4 byte thành số nguyên
            integer_value = struct.unpack('I', binary_data)[0]
            print(f"Số nguyên từ 4 byte là: {integer_value}")
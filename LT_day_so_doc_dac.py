def count_pythagorean_triplets(N):
    count = 0

    # Tạo một danh sách chứa bình phương modulo N của từng số nguyên từ 0 đến N-1
    squares_mod_N = [(i * i) % N for i in range(N)]

    for a in range(1, N):
        for b in range(a, N):
            c_square_mod_N = (squares_mod_N[a] + squares_mod_N[b]) % N

            # Tìm c bằng cách kiểm tra nếu c_square_mod_N là bình phương modulo N
            for c in range(1, N):
                if (c * c) % N == c_square_mod_N:
                    count += 1

    return count

N = 500 # Thay đổi giá trị của N tùy theo yêu cầu của bạn
result = count_pythagorean_triplets(N)
print(f"Số bộ 3 số thỏa mãn: {result}")

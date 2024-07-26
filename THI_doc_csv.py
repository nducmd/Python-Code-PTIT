import csv
with open("flights.csv") as file:
    doc_csv = csv.reader(file)
    
    du_lieu = list(doc_csv)
    
    so_hang = len(du_lieu)
    so_cot = len(du_lieu[0])
    print(so_hang, so_cot)

with open("filecsv.csv", "w", newline = "") as file1:
    ghi_csv = csv.writer(file1)
    ghi_csv.writerows(du_lieu)
    
import csv

# Tên tệp CSV bạn muốn đọc
ten_tep_csv = 'danhsach.csv'

# Mở tệp CSV để đọc
with open(ten_tep_csv, newline='', encoding='utf-8') as file:
    # Tạo đối tượng đọc CSV
    doc_csv = csv.reader(file)
    print(type(doc_csv))
    # Chuyển đổi đối tượng đọc CSV thành danh sách
    du_lieu = list(doc_csv)

# In kiểu dữ liệu của các giá trị trong tệp CSV
for dong in du_lieu:
    for gia_tri in dong:
        print(f"{gia_tri}: {type(gia_tri)}")

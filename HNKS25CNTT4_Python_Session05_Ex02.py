# code gốc
# branch_count = int(input("Nhập số lượng chi nhánh: "))
# class_count = int(input("Nhập số lớp học của mỗi chi nhánh: "))

# total_students = 0

# for branch in range(1, branch_count + 1):
#     print(f"\nChi nhánh {branch}")

#     for classroom in range(1, class_count + 1):
#         student_count = int(input(f"Nhập số học viên lớp {classroom}: "))
#         total_students += student_count

#     print(f"Chi nhánh {branch}: {total_students} học viên")

# Phân tích lỗi:
# Giả sử:
# Chi nhánh 1: Lớp 1 có 40 học viên, Lớp 2 có 43 học viên => Tổng đúng = 83
# Vẫn hiển thị đúng vì chương trình mới bắt đầu chạy, biến total_students được khởi tạo bằng 0 lúc này mới bắt đầu tính toán nên 0 + 40 + 43 = 83, trả về đúng 83
# Chi nhánh 2: Lớp 1 có 30 học viên, Lớp 2 có 30 học viên => Tổng đúng = 60
# Nhưng hệ thống hiển thị 143 vì lúc này biến total_students đã có giá trị là 83 rồi nên khi chạy nó vẫn tiếp tục cộng dồn lại 83 + 60 = 143, trả về 143
# Chi nhánh 3: Lớp 1 có 50 học viên, Lớp 2 có 47 học viên => Tổng đúng = 97
# Cũng tương tự vậy lúc này biến total_students đã có giá trị là 143 rồi nên nó vẫn tiếp tục cộng dồn 83 + 97 = 270, trả về 270

# Sửa
branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của mỗi chi nhánh: "))

for branch in range(1, branch_count + 1):
    print(f"\nChi nhánh {branch}")
    
    total_students = 0   # Khai biến ở đây để Reset về 0 mỗi khi bắt đầu một chi nhánh mới

    for classroom in range(1, class_count + 1):
        student_count = int(input(f"Nhập số học viên lớp {classroom}: "))
        total_students += student_count

    # Bây giờ kết quả in ra sẽ độc lập và chính xác tuyệt đối
    print(f"Chi nhánh {branch}: {total_students} học viên")
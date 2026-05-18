# input
#  tên bệnh nhân,Mã bệnh án,Khoa / Phòng khám	sử dụng kiểu str 

# output
# Bệnh nhân: Nguyễn Văn A - Mã BA: BA1024 - Chuyển tới: Khoa Nội

# giải pháp
#1.Hiển thị tiêu đề chương trình
#2.Nhập thông tin bệnh nhân
#3.Lưu dữ liệu vào biến
#4.Sử dụng f-string để xuất dữ liệu theo đúng định dạng yêu cầu

print("--- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ---")
ho_ten = input("Nhập họ tên bệnh nhân: ")
ma_ba = input("Nhập mã bệnh án: ")
khoa_phong = input("Nhập khoa/phòng khám: ")
print("\n--- PHIẾU KHÁM BỆNH ĐIỆN TỬ ---")
print(f"Bệnh nhân: {ho_ten} - Mã BA: {ma_ba} - Chuyển tới: {khoa_phong}")
print("Tiếp nhận bệnh nhân thành công!")
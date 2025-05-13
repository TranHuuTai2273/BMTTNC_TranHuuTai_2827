#Tạo một danh sách rỗng để lưu Kết quả
j = []
# Duyệt qua tất cả cấc số
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 !=0):
        j.append(str(i))
import time
import os
import sys


list_user_name = []
list_password = []
list_time_create = []
#lấy dữ  liệu từ file
with open("data/taikhoan.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        list_user_name.append(lines[i].strip())
        list_password.append(lines[i+1].strip())
        list_time_create.append(lines[i+2].strip())

#đổi mật khẩu
def change_password():
    user_name = input("Nhập tên đăng nhập của bạn: ")
    if user_name in list_user_name:
        password = input("Nhập mật khẩu cũ: ")
        if password == list_password[list_user_name.index(user_name)]: 
            vitri = list_user_name.index(user_name)
            new_password = input("Nhập mật khẩu mới: ")
            list_password[vitri] = new_password
            with open("data/taikhoan.txt", 'w', encoding='utf-8') as file:
                for i in range(len(list_user_name)):
                    file.write(list_user_name[i] + '\n' + list_password[i] + '\n')
            print("Đổi mật khẩu thành công!")
        else:
            print("Mật khẩu cũ không đúng!")
            os.system("cls")
            change_password()
    else:
        print("Tên đăng nhập không tồn tại!")
        change_password()
#xem thông tin tài khoản
def view_account_info():
    user_name = input("Nhập tên đăng nhập: ")
    if user_name in list_user_name:
        print("Tên đăng nhập: ", user_name)
        print("Mật khẩu: ", list_password[list_user_name.index(user_name)])
        print("Thời gian tạo: ", list_time_create[list_user_name.index(user_name)])
    else:
        print("Tên đăng nhập không tồn tại!")
        view_account_info()

#danh sách tài khoản

def account_list():
    print("============================")
    print("      DANH SÁCH TÀI KHOẢN      ")
    print("============================")
    print()
    for i in range(len(list_user_name)):
        print("Tên đăng nhập: ", list_user_name[i])
        print("Mật khẩu: ", list_password[i])
        print("-------------------------")


#hiển thị menu quản lý tài khoản
def admin_menu():

    print("============================")
    print("      QUẢN LÝ TÀI KHOẢN      ")
    print("============================")
    print()
    print("1. Thay đổi mật khẩu")
    print("2. Xem thông tin tài khoản")
    print("3. Danh sách tài khoản")
    print("4. Thoát")

    print("============================")
    choice = input("Chọn chức năng: ")
    if choice == '1':
        os.system("cls")
        print("============================")
        change_password()
        enter = input("Nhấn Enter để tiếp tục: ")
        os.system("cls")
        admin_menu()
    elif choice == '2':
        os.system("cls")
        print("============================")
        view_account_info()
        enter = input("Nhấn Enter để tiếp tục: ")
        os.system("cls")
        admin_menu()
    elif choice == '3':
        os.system("cls")
        print("============================")
        account_list()
        enter = input("Nhấn Enter để tiếp tục: ")
        os.system("cls")
        admin_menu()
    elif choice == '4':
        print("Đang thoát...")
        time.sleep(1)
        os.system('python main.py')
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
        os.system("cls")
        admin_menu()
admin_menu()
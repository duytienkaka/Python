import getpass
import os 
import time
import sys
from datetime import datetime
def sign_up():
    print("                         Đăng ký tài khoản")
    user_name = input("Nhập tên đăng ký: ")
    password = input("Nhập mật khẩu: ")
    confirm_password = input("Nhập lại mật khẩu: ")
    if password != confirm_password:
        print("⚠ Mật khẩu không trùng khớp. Vui lòng thử lại.")
        os.system("cls")
        sign_up()
    else:
        print("Đăng ký thành công!")
        time_create = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("data/taikhoan.txt",'a',encoding = 'utf-8') as f:
            f.write(user_name + "\n") 
            f.write(password + "\n")
            f.write(time_create + "\n")
        print("Hãy đăng nhập để chuyển tiếp đến trang chủ!")
        print("Bạn có muốn đăng nhập không (Có / Không)?", end="")
        answer = input("").strip()
        if answer.lower() == 'có':
            sign_in()
        elif answer.lower() == "không":
            print("Hẹn gặp lại!")
            sys.exit()
        else:
            os.system("cls")
            print("⚠ Lựa chọn không hợp lệ. Vui lòng thử lại.")
            sign_up()

def sign_in():
    print("                         Đăng nhập")
    user_name = input("Nhập tên đăng nhập: ")
    password = input("Nhập mật khẩu: ")
    with open("data/taikhoan.txt", 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
        if user_name == lines[0].strip() and password == lines[1].strip():
            print("Đăng nhập thành công!")
            time.sleep(1)
            os.system('python main.py')
        else:
            os.system("cls")
            print("⚠ Tên đăng nhập hoặc mật khẩu không đúng. Vui lòng thử lại.")
            sign_in()

def main():
    print("=====================================")
    print("      CHÀO MỪNG ĐẾN VỚI ỨNG DỤNG      ")
    print("=====================================")
    print()
    print("Bạn đã có tài khoản hay chưa?")
    print("-------------------------------------")
    print("1. Có")
    print("2. Chưa")
    print("-------------------------------------")
    
    answer = input("Vui lòng nhập lựa chọn của bạn (1 hoặc 2): ").strip()

    print()
    print("=====================================")
    
    if answer == '1':
        print("✔ Đang chuyển tiếp đến trang Đăng nhập...")
        time.sleep(1)
        sign_in()
    elif answer == '2':
        print("✔ Đang chuyển tiếp đến trang Đăng ký...")
        time.sleep(1)
        sign_up()
    else:
        print("⚠ Lựa chọn không hợp lệ. Vui lòng thử lại.")
        os.system("cls")
        main()
    
    print("=====================================")
    
main()

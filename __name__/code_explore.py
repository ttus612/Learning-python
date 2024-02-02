def welcome():
    print("Welcome to the code explore module")

def function1():
    print("Function 1 executed")

def main():
    welcome()
    function1()

# hàm main sẽ được gọi khi chạy module này là file chính 
# Nó được bảo về bởi __name__ == "__main__"
# Nếu module này được import vào module khác thì hàm main sẽ không được gọi
if __name__ == "__main__":
    main()  
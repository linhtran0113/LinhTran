# for i in range (26):
#     print(i)

# for i in range(0, 101, 2):
#     print(i)

#print(*range(1, 10, 2))

# for i in ['a', 'b','c']:
#     print(i)

# n = int(input("enter the number"))
# total = 0
# for i in range(n + 1):
#     total = total + i
# print(total)2


# username = 'mindx'
# password = 'password'
# while True :
#     username_input = input("Username :")
#     password_input = input("Password :")
#     if username_input == username and password_input == password:
#         print("Welcome")
#         break

# from getpass import getpass
username = 'mindx'
password = 'password'
count = 0
while True :
    if count > 7:
        print("Het lan nhap")
        break
    username_input = input("Username :")
    password_input = input("Password :")
    if username_input == username and password_input == password:
        print("Welcome")
        break
    else:
        count += 1






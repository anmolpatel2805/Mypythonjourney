# # 🟢 DAY 2 – Variables & Data Types
# #
# # (int, float, string, boolean, type casting, IP & port)
# #
# # 1️⃣ Store your age in a variable and print it.
# # age = 22
# # print(age)
# #
# # 2️⃣ Store your height (in meters) as a float and print its type.
# # height = 5.4
# # print(type(height))
# #
# # 3️⃣ Store your name in a string and print it.
# # name = "Anmol"
# # print(name)
# #
# # 4️⃣ Store whether you are logged in using a boolean and print it.
# # is_logged_in = True
# # print(is_logged_in)
# #
# # 5️⃣ Take a number as input and convert it to integer.
# # num = input("Enter a number: ")
# # num = int(num)
# # print(num)
# #
# # 6️⃣ Store an IP address as a string and print it.
# # ip_address = "192.168.1.1"
# # print(ip_address)
# #
# # 7️⃣ Store a port number and print its data type.
# # port = 8080
# # print(type(port))
# #
# # 8️⃣ Add two integers and print the result.
# # a = 10
# # b = 20
# # print(a + b)
# #
# # 9️⃣ Convert a float into an integer and print both.
# # x = 7.9
# # y = int(x)
# # print(x)
# # print(y)
# #
# # 🔟 Store IP and port together and print them.
# # ip = "127.0.0.1"
# # port = 80
# # print(ip, port)
# 🟢 DAY 3 – Input & Output
#
# (input(), type conversion, user IP input)
#
# 1️⃣ Take your name as input and print it.
# name = input("Enter your name: ")
# print(name)
#
# 2️⃣ Take age as input and print its type.
# age = input("Enter age: ")
# print(type(age))
#
# 3️⃣ Convert user age into integer and print it.
# age = int(input("Enter age: "))
# print(age)
#
# 4️⃣ Take two numbers from user and print their sum.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(a + b)
#
# 5️⃣ Take an IP address from user and print it.
# ip = input("Enter IP address: ")
# print(ip)
#
# 6️⃣ Take port number from user and convert it to integer.
# port = int(input("Enter port number: "))
# print(port)
#
# 7️⃣ Take username and password and print both.
# username = input("Enter username: ")
# password = input("Enter password: ")
# print(username, password)
#
# 8️⃣ Take float value from user and print it.
# value = float(input("Enter a float value: "))
# print(value)
#
# 9️⃣ Take a boolean-like input and print it as string.
# status = input("Enter status (True/False): ")
# print(status)
#
# 🔟 Take IP and port from user and print them.
# ip = input("Enter IP: ")
# port = int(input("Enter port: "))
# print(ip, port)
#
# 🟢 DAY 4 – Conditional Statements
#
# (if, if-else, if-elif-else, login checker)
#
# 1️⃣ Check if a number is positive.
# num = int(input("Enter number: "))
# if num > 0:
#     print("Positive number")
#
# 2️⃣ Check if a number is even or odd.
# num = int(input("Enter number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
#
# 3️⃣ Check if age is eligible to vote.
# age = int(input("Enter age: "))
# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible")
#
# 4️⃣ Check if port number is valid (0–65535).
# port = int(input("Enter port: "))
# if 0 <= port <= 65535:
#     print("Valid port")
# else:
#     print("Invalid port")
#
# 5️⃣ Check login using correct username.
# username = input("Enter username: ")
# if username == "admin":
#     print("Login successful")
# else:
#     print("Login failed")
#
# 6️⃣ Check login using username and password.
# username = input("Enter username: ")
# password = input("Enter password: ")
#
# if username == "admin" and password == "1234":
#     print("Login successful")
# else:
#     print("Invalid credentials")
#
# 7️⃣ Check grade using marks.
# marks = int(input("Enter marks: "))
#
# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 60:
#     print("Grade C")
# else:
#     print("Fail")
#
# 8️⃣ Check if IP is local or public.
# ip = input("Enter IP: ")
#
# if ip == "127.0.0.1":
#     print("Localhost IP")
# else:
#     print("Public IP")
#
# 9️⃣ Login attempt checker (single attempt).
# password = input("Enter password: ")
#
# if password == "python123":
#     print("Access granted")
# else:
#     print("Access denied")
#
# 🔟 Check if number is between 10 and 50 but not 30.
# num = int(input("Enter number: "))
#
# if 10 <= num <= 50 and num != 30:
#     print("Valid number")
# else:
#     print("Invalid number")
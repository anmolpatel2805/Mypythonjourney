# 🟢 DAY 5 – Logical Operators
#
# (AND, OR, NOT, Multiple condition checks)
#
# 1️⃣ Check if a number is greater than 10 AND less than 50.
# num = int(input("Enter number: "))
# if num > 10 and num < 50:
#     print("Number is between 10 and 50")
#
# 2️⃣ Check if a number is divisible by 2 OR divisible by 5.
# num = int(input("Enter number: "))
# if num % 2 == 0 or num % 5 == 0:
#     print("Number is divisible by 2 or 5")
#
# 3️⃣ Check if a user is NOT an admin.
# username = input("Enter username: ")
# if not username == "admin":
#     print("User is not admin")
#
# 4️⃣ Check login using AND operator.
# username = input("Enter username: ")
# password = input("Enter password: ")
#
# if username == "admin" and password == "1234":
#     print("Login successful")
#
# 5️⃣ Check if age is between 18 and 60 using AND.
# age = int(input("Enter age: "))
# if age >= 18 and age <= 60:
#     print("Valid age")
#
# 6️⃣ Check if a port is valid OR equals 8080.
# port = int(input("Enter port: "))
# if (0 <= port <= 65535) or port == 8080:
#     print("Port allowed")
#
# 7️⃣ Check if a number is NOT negative.
# num = int(input("Enter number: "))
# if not num < 0:
#     print("Number is not negative")
#
# 8️⃣ Check if IP is localhost AND port is 80.
# ip = input("Enter IP: ")
# port = int(input("Enter port: "))
#
# if ip == "127.0.0.1" and port == 80:
#     print("Local server running")
#
# 9️⃣ Check if marks are valid (0–100).
# marks = int(input("Enter marks: "))
# if marks >= 0 and marks <= 100:
#     print("Valid marks")
#
# 🔟 Check if a number is divisible by 3 AND NOT divisible by 5.
# num = int(input("Enter number: "))
# if num % 3 == 0 and not num % 5 == 0:
#     print("Condition satisfied")
#
# 🟢 DAY 6 – For Loop
#
# (Loop syntax, iterate list of IPs)
#
# 1️⃣ Print numbers from 1 to 5.
# for i in range(1, 6):
#     print(i)
#
# 2️⃣ Print even numbers from 1 to 10.
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)
#
# 3️⃣ Print each character of a string.
# text = "Python"
# for ch in text:
#     print(ch)
#
# 4️⃣ Print all elements of a list.
# numbers = [1, 2, 3, 4]
# for num in numbers:
#     print(num)
#
# 5️⃣ Iterate through a list of IP addresses.
# ips = ["192.168.1.1", "10.0.0.1", "127.0.0.1"]
# for ip in ips:
#     print(ip)
#
# 6️⃣ Print numbers from 0 to 4 using range.
# for i in range(5):
#     print(i)
#
# 7️⃣ Print square of numbers from 1 to 5.
# for i in range(1, 6):
#     print(i * i)
#
# 8️⃣ Print only localhost IP from a list.
# ips = ["192.168.1.10", "127.0.0.1", "8.8.8.8"]
#
# for ip in ips:
#     if ip == "127.0.0.1":
#         print("Localhost found")
#
# 9️⃣ Calculate sum of numbers from 1 to 5.
# total = 0
# for i in range(1, 6):
#     total += i
# print(total)
#
# 🔟 Print multiplication table of 5.
# for i in range(1, 11):
#     print(5 * i)
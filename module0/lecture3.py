# Task 1

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible")

# Task 2

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Task 3

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Task 4

username = "admin"
password = "python123"
input_username = input("Enter username: ")
input_password = input("Enter password: ")
if input_username == username and input_password == password:
    print("Login Successful")
else:
    print("Invalid Credentials")



# Mini Project (Student Result System)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))

grade = ""
status = ""

if marks >= 90:
    grade = "A"
    status = "Pass"
elif marks >= 70:
    grade = "B"
    status = "Pass"
elif marks >= 50:
    grade = "C"
    status = "Pass"
else:
    grade = "D"
    status = "Fail"

print(f""" 
Hello {name}
Marks: {marks}
Grade: {grade}
Status: {status}
""")

if marks >= 90:
    print("Excellent performance!")



# Mentor Challenge

# Q1:  B
# Q2: False
# Q3:  True
# Q4:  = is assignment operator and == is comparion operator



# Bonus Interview Question

# Python choose indentation to make the code readable and to define the scope of loops, functions, classes, and conditionals. Indentation is crucial in Python as it indicates a block of code.
 
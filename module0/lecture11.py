# Task 1

try:
    num = int(input("Enter Number: "))
    result = 100 / num
    print(result)

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program Finished")

# Ran with 10, 0 and abc getting output like "10.0", "cannot divide by zero" and "please enter a valid number"
# yes finally is running in each case.

# Task 3

def divide(a, b):
    try:
        c = a/b
        return c
    except:
        return "Invalid division"
    

# Mentor Challenge 1
# 1. A, C, D

# Mentor Challenge 2
# 100, Success, Done


# Homework

# Exception handling is used to handle the exceptions like "ZeroDivisionError" or any db RELATED ERROR if we got during implemention that it will catch by this.
# except is handing exception means if any exception come than it will be caught by except. else is used in any condition task. and finally is used to perform any task at final stage whether any exception came or not it will run definitely.
# DB connection close krna is a good way at finally block.


# Weekend Mini Project (Smart Calculator)

class Calculator:
    def __init__(self):
        pass
    def add(self, a, b):
        try:
            return a + b
        except ValueError:
            return "Please enter valid number"
        except:
            return "Something went wrong"
    def subtract(self, a, b):
        try:
            return a - b
        except ValueError:
            return "Please enter valid number"
        except:
            return "Something went wrong"
        
    def multiply(self, a, b):
        try:
            return a * b
        except ValueError:
            return "Please enter valid number"
        except:
            return "Something went wrong"
    def division(self, a, b):
        try:
            return a / b
        except ValueError:
            return "Please enter valid number"
        except ZeroDivisionError:
            return "cannot divide by zero"
        except:
            return "Something went wrong"
        
def performCalculation(num1, num2, operation):
    while operation:
        if operation == "add":
            return calculator.add(num1, num2)   
        elif operation == "subtract":
            return calculator.subtract(num1, num2)
        elif operation == "multiply":
            return calculator.multiply(num1, num2)
        elif operation == "divide":
            return calculator.division(num1, num2)
        else:
            print("Please enter correct operation type from add, subtract, multiply and divide")
            return

calculator = Calculator()
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("opration do you want to perform: ")

        
result = performCalculation(num1, num2, operation)
print(result)




    




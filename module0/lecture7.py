# Classes

# Task 1

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Task 2
    def show_detail(self):
        print(f"""
       Name: {self.name}
       Age: {self.age}
    """)

# Task 3  
student_1 = Student("Uday", 22)
student_2 = Student("Rahul", 21)

student_1.show_detail()
student_2.show_detail()

# Task 4

class Calculator:
    
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
calc = Calculator()
print(calc.add(10, 5))
print(calc.subtract(10, 5))


# Mentor Challenge

# Output: "Woof", "Woof"


# Challenge 2

# It will give an error because we have not passed self parameter in the method definition. The first parameter of a method should always be self, which refers to the instance of the class.


# Homework Reflection

# Class is a blueprint for creating objects. and object is an instance of a class. A class can have attributes (variables) and methods (functions) that define the behavior of the objects created from the class.
# self is a reference to the current instance of the class and is used to access variables and methods associated with the current object. It is passed automatically when a method is called on an object, but it must be explicitly included as the first parameter in the method definition.
# real life example of OOPS is a car. A car can be represented as a class with attributes like color, model, and speed, and methods like start(), stop(), and accelerate(). Each individual car (object) created from the Car class can have its own unique values for these attributes and can perform the actions defined by the methods.
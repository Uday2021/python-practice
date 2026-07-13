# Task 1

def add():
    print(10 + 20)

operation = add

operation()


# Task 2

def outer():
    print("Outer started")
    def inner():
        print("inner started")
    
    inner()
    print("outer finished")

outer()


# Task 3

def teacher():
    def student():
        print("Learning Python")
    student()

teacher()


# Mentor Challenge 1. -- functional object of type "hello"
# Mentor Challenge 2  -- A, C
# Homework. -- 1. greet can be a variable or object and greet() is a function calling
# Homework. -- 2. first class object might be because we are using functions in class by creating an instance object of class.
# Homework. -- 3 real life example ho skta hai if we want to use the same function in different modules/files than we can export it with the help of variable and we can export that variable and use/call that anywhere.

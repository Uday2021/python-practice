# Task 1

def decorator(func):

    def wrapper(*args, **kwargs):

        print("Start")

        result = func(*args, **kwargs)

        print("End")

        return result

    return wrapper

@decorator
def multiply(a, b):
    return a * b

multiply(20,30)

@decorator
def introduce(name, age):

    print(name)

    print(age)

introduce("Uday", 30)



# Mentor Challenge 1. -- >  expected 0 argument but passing 1 error
# Mentor Challenge 2. -- > (10,20), 30

# Homework
# 1. *args is kind of data representation as touple and **kwargs is kind of data representation as dictionary.
# 3. return result nhi kroge to decorator kbhi return nhi krega and wo usse bahar nhi nikal payega.



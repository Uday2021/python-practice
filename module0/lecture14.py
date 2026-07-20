# Task 1

def decorator(func):

    def wrapper():
        print("Start")

        func()

        print("End")

    return wrapper


# Task 2

def study():
    print("Learning AI")

study = decorator(study)
study()


#  Task 3

@decorator
def work():
    print("Writing code")

work()

# Mentor Challenge 1  --  1, 2, 3

# Mentor Challenge 2. -- "Before" and it returns wrapper function

# Home work

# 1. decorator is a king of wrapup which include/ add on some functionality on function
# ye dono same h because kaam dono ka same h bs represent krne ke liye easy wo @ lga dete h aage.
# Fast API me backend likhte time


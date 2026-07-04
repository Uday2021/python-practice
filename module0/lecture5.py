# Task 1

def greet():
    print("Welcome to python bootcamp!")

greet()

# Task 2

def greet(name):
    print(f"Hello {name}!")

greet("Uday")

# Task 3

def square(number):
    return number * number

result = square(5)
print(result)


# Task 4

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
is_even_result = is_even(4)
print(is_even_result)

# Task 5

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"
    
grade = calculate_grade(85)
print(grade)


# Saturday Mega Project (Number Guessing Game)

def generate_random_number():
    import random
    return random.randint(1, 100)

def get_user_guess():
    guess = int(input("Enter your guess (between 1 and 100): "))
    return guess

def check_guess(random_number, user_guess):
    if user_guess < random_number:
        print("Too low! Try again.")
    elif user_guess > random_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")

def play_again():
    choice = input("Do you want to play again? (yes/no): ")
    if choice.lower() == "yes":
        main()
    else:
        print("Thank you for playing!")


def main():
    
    random_number = generate_random_number()
    user_guess = get_user_guess()
    check_guess(random_number, user_guess)
    play_again()

main()


# Saturday Research Question

# 1. Print is a standalone function in python but append is a method of list.
# 2. Print is a standalone function in python but append is a method of list.



# Quick revision

# 1. 20, 10
# 2. 22
# 3. 1,2,3
# 4. 1,2,4,5



# Number guessing game V2

def generate_random_number():
    import random
    return random.randint(1, 100)

def get_user_guess():
    guess = int(input("Enter your guess (between 1 and 100): "))
    return guess

def check_guess(secret_number, user_guess):
    while user_guess != secret_number:
        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        user_guess = int(input("Enter your guess (between 1 and 100): "))
    print(f"Congratulations! You've guessed the number {secret_number} correctly!")

def play_game():
    secret_number = generate_random_number()
    user_guess = get_user_guess()
    check_guess(secret_number, user_guess)

def ask_play_again():
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            play_game()
        elif play_again == "no":
            print("Thank you for playing! Goodbye!")
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def main():
   while True:
       play_game()
       if not ask_play_again():
           break

# main()


# Interview Round

# 1. import math is basically we are importing the math module and we can use the functions and constants defined in the math module. and from math import sqrt means we are importing only the sqrt function from the math module and we can use it directly without prefixing it with math.
# 2. yes each python file is a module and we can import it in another python file using import statement. and we can use the functions and variables defined in that module.
# 3. random.randint(1, 10) generates a random integer between 1 and 10 (inclusive). so here 1 and 10 is also included in the range of random numbers generated.\

import math

print(math)

# this will print the math module and its path where it is located in the system.


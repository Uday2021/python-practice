# Task 1

class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def eat(self):
        print(f"{self.name} is eating.")

    def speak(self):
        print("Some sound")

    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Breed : {self.breed}")

# Task 2, 3 4

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, breed)

    def bark(self):
        print("Woof!")
    
    def speak(self):
        print("Woof")

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, breed)
    
    def speak(self):
        print("Meow")


dog = Dog("Bruno", "Labrador")
dog.eat()
dog.bark()
dog.show_details()


# Mentor Challenge

# 1. Dog

# Final Boss

# 1. Animal
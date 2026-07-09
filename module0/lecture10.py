# Polymorphism

# Task 1

class Dog:
    def __init__(self):
        pass

    def speak(self):
        print("Bark")

class Cat:
    def __init__(self):
        pass

    def speak(self):
        print("Meow")

class Robot:
    def __init__(self):
        pass

    def speak(self):
        print("Hello Human")

def make_sound(obj):
    obj.speak()

make_sound(Dog())

make_sound(Cat())

make_sound(Robot())


# Mentor Challenge 1. --> Flying, Jet Engine
# Mentor Challenge 2. --> 4, 3, 1 (len() same method hote huye bhi alag alag objects ke liye kaam kr rha h due to polymorphism. means agar dhang se explain kru to based on the type/value we are passing it is finding the result it is actually passing like instance of string and list and object.)

# Weekend Bonus Challenge

class Singer:
    def speak(self):
        print("I sing songs")

make_sound(Singer())


# Polymorphism is a multiform of any object to do different behaviour with same method. like above make_sound is the generic method which is calling everytime the same method speak and result is everytime not coming same it is coming as per the instance passed in that method and the attached speak method to that instance is calling.
# the same thing I explained in first it is duck point also.
# method overloading --> no idea
# real like example of polymorphism is power on button the button is same for different appliences but behaviour of all applience can e different.
# Task 1

def numbers():

    yield 10

    yield 20

    yield 30

for i in numbers():
    print(i)

# it will print 10, 20, 30

# Task 2
def even():

    yield 2

    yield 4

    yield 6

    yield 8

x = even()
for i in x:
    print(i)
# It will print 2, 4, 6, 8

# Task 3

def demo():

    print("Start")

    yield 100

    print("Middle")

    yield 200

    print("End")

g = demo()

print(next(g))

print(next(g))

# It will print start, 100, Middle, 200


# Mentor Challenge 1. --- AI, AWS

# Mentor Challenge 2 (Brain Teaser). --- 1, 2, 3, 10, 20

# Homework. -- 1. return function complete hote hi flush out/destroy ho jata h. but yeild function complete hone pr pause ho jata h we can access again.
# generator object is not but the yield which is return by generator function.
# AI me generator ka use large data ko handle krne ke liye because at a time large data ko we cant handle without using generator yield. because we can stream data partially using yield not at a time.
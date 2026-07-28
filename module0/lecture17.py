nums = [5, 10, 15]

it = iter(nums)

print(next(it))
print(next(it))
print(next(it))

# 5, 10, 15

# Task 2

square = (x*x for x in range(6))

for i in square:
    print(i)

# 0, 1, 4, 9, 16, 25


# Task 3

a = [x for x in range(5)]

b = (x for x in range(5))

print(type(a))
print(type(b))

# List and second one is of type Genrator object


# Mentor Challenge 1

nums = [1, 2]

it = iter(nums)

print(next(it))

print(next(it))

print(next(it))

# 1, 2, StopIteration

# Mentor Challenge 2

g = (x for x in range(3))

print(next(g))

print(list(g))

# 0, [1,2]


# Homework
# 1. Iterator is basically a way to iterate the list and objects. here in case of generator iterator iterate the elements partially means one by one and thats why it is memory efficient.
# 2. Generator expression and list comprehension me difference ye h ki list comprehension me saari values ek saath memory me and generator expression me ek ek krke values jati h so memory effiecient.
# 3. the same reason because it iterates the values one after one thats why it is memory efficient.
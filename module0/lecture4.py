# Task 1

for number in range(1, 21):
    print(number)

# Task 2

for number in range(1, 21):
    if number % 2 == 0:
        print(number)

# Task 3

for number in range(1, 21):
    if number % 2 != 0:
        print(number)

# Task 4

for number in range(10, 0, -1):
    print(number)

# Task 5

skills = [
    "Python",
    "NodeJS",
    "AWS",
    "Docker"
]

for skill in skills:
    print(skill)


# Task 6

count = 1

while count <= 10:
    print(count)
    count += 1


# Mini Project (Student Management System)

students = [
    "Rahul",
    "Uday",
    "Amit",
    "Priya",
    "Neha"
]

count = 1
for student in students:
    print(f"Student {count}: {student}")
    count += 1
print("Total students:", len(students))


# Saturday Interview Round

# Q1: 0
# Q2: 0,1,2
# Q3: 0,1,2,4
# Q4: break is actually used to exit from the loop, while continue is used to skip the current iterationand move to next one.
# Q5: (0,0),(0,1),(1,0),(1,1)


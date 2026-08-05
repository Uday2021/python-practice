# Task 1

import pandas as pd

df = pd.DataFrame({
    "Name": ["Uday","Rahul","Amit"],
    "Age": [30,28,31],
    "Salary": [90000,75000,82000]
})

print(df)

# Output:
#     Name  Age  Salary
# 0   Uday   30   90000
# 1  Rahul   28   75000
# 2   Amit   31   82000 

# Task 2

print(df.shape)
print(df.columns)
print(df.size)
print(df.dtypes)

# Output:
# (3, 3)
# Index(['Name', 'Age', 'Salary'], dtype='object')
# 9
# Name       object
# Age         int64
# Salary      int64

# Task 3

print(df.head())

print(df.head(2))

print(df.tail(1))

# Output:
#     Name  Age  Salary
# 0   Uday   30   90000
# 1  Rahul   28   75000
# 2   Amit   31   82000

# Output:
#     Name  Age  Salary
# 0   Uday   30   90000
# 1  Rahul   28   75000

# Output:
#     Name  Age  Salary
# 2   Amit   31   82000

# Task 4

print(df["Name"])

print(df[["Name","Salary"]])

# Output:
# 0     Uday
# 1    Rahul
# 2     Amit

# Output:
#     Name  Salary
# 0   Uday   90000
# 1  Rahul   75000
# 2   Amit   82000

# Mentor Challenge 1

print(df.shape)

# Output: (3, 3)

# Mentor Challenge 2

print(df["Age"])

# Output:
# 0    30
# 1    28
# 2    31

# Mentor Mega Challenge

print(df[["Age","Salary"]].shape)

# Output: (3, 2)

# Homework

# Create your own DataFrame: 
# Name
# Course
# Experience
# Company

d = pd.DataFrame({
    "Name": ["Uday", "Rahul", "Amit"],
    "Course": ["Python", "Data Science", "Machine Learning"],
    "Experience": [5, 3, 4],
    "Company": ["ABC Corp", "XYZ Ltd", "PQR Inc"]
})
print(d)

print(d.shape)
# Output: (3, 4)
print(d.head())
# it will fetch or return top 5 rows of the DataFrame by default.
print(d.tail(2))
# it will fetch or return last 2 rows of the DataFrame.
print(d.columns)
# Output:
# Index(['Name', 'Course', 'Experience', 'Company'], dtype='object')
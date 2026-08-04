# Task 1

import pandas as pd

marks = pd.Series([10,20,30,40])

print(marks)

# 0,1,2,3 and 10,20,30,40 are index and values of the series respectively. and datatype of the series is int64.

# Task 2

students = pd.Series(
    [90,85,95],
    index=["Uday","Rahul","Amit"]
)

print(students)

# "Uday", "Rahul", "Amit" are index and 90, 85, 95 are values of the series respectively. and datatype of the series is int64.

# Task 3

print(students["Rahul"])
print(students.shape)
print(students.size)
print(students.dtype)

# 85, (3,), 3, int64 are the output of the above code respectively.


# Mentor Challenge 1

import pandas as pd

s = pd.Series([5,10,15])

print(s[1])

# Output: 10

# Mentor Challenge 2

s = pd.Series(
    [100,200],
    index=["A","B"]
)

print(s["B"])

# Output: 200

# Mentor Mega Challenge

import pandas as pd

s = pd.Series(
    [10,20,30],
    index=["x","y","z"]
)

print(s.shape)
print(s.size)

# Output: (3,) and 3

# Homework

# Create your own Series:
# Name : Uday
# Age  : 30
# City : Delhi
# Salary : 90000

s = pd.Series(
    [ "Uday", 30, "Delhi", 90000],
    index=["Name", "Age", "City", "Salary"])
print(s)



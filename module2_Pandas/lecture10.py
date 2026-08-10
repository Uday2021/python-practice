# Task 1
import pandas as pd

df = pd.DataFrame({
    "Name": ["Uday", "Rahul", "Amit"],
    "Salary": [90000, 75000, 82000]
})

df["Salary"] = df["Salary"].apply(
    lambda x: x * 1.10
)

print(df)
# Output:
#   Name Salary
# 0 Uday 99000
# 1 Rahul 82500
# 2 Amit 90200

# Task 2
s = pd.Series([10, 20, 30, 40])

print(
    s.apply(lambda x: x * 2)
)

#  20, 40, 60, 80

# Task 3
df = pd.DataFrame({
    "Name": ["Uday", "Rahul", "Amit", "Neha"],
    "Age": [30, 17, 31, 15]
})

df["Category"] = df["age"].apply(lambda x: "Adult" if x >= 18 else "Minor")

# Mentor Challenge 1
s = pd.Series([5, 10, 15])

print(
    s.apply(lambda x: x + 10)
)

# 15, 20, 25

# Mentor Challenge 2

s = pd.Series([2, 3, 4])

print(
    s.apply(lambda x: x ** 2)
)

# 4, 9, 16

# Mentor Mega Challenge
df = pd.DataFrame({
    "Name": ["Uday", "Rahul", "Amit"],
    "Salary": [50000, 80000, 120000]
})

df["Level"] = df["Salary"].apply(
    lambda x: "High" if x >= 80000 else "Low"
)

print(df)

#  Name Salary Level
# 0 Uday 50000 Low
# 1 Rahul 80000 High
# 2 Amit 120000 High



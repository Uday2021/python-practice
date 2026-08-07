# Task 1
import pandas as pd

df = pd.DataFrame({
    "Name": ["Uday", "Rahul", "Amit", "Neha", "Pooja"],
    "Age": [30, 28, 31, 26, 28],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [90000, 75000, 82000, 68000, 76000]
})

print(df.sort_values("Salary"))
# Output:
#     Name   Age Department  Salary
# 0   Uday  30.0         IT  90000
# 2   Amit  31.0         IT  82000
# 4   Pooja  28.0         HR  76000
# 1   Rahul  28.0         HR  75000
# 3   Neha  26.0    Finance  68000

# Task 2
print(df.sort_values("Age", ascending=False))

# Output:
#     Name  Age Department  Salary
# 2   Amit   31         IT  82000
# 0   Uday   30         IT  90000
# 1  Rahul   28         HR  75000
# 4  Pooja   28         HR  76000
# 3   Neha   26    Finance  68000

# Task 3
print(df["Department"].unique())
# Output:
# ['IT' 'HR' 'Finance']

print(df["Department"].nunique())
# Output:
# 3

# Task 4
print(df["Department"].value_counts())
# Output:
# IT         2
# HR         2
# Finance    1

# Mentor Challenge 1
print(df["Age"].unique())
# Output:
# [30 28 31 26]

# Mentor Challenge 2
print(df["Age"].nunique())
# Output:
# 4

# Mentor Mega Challenge
print(
    df[
        df["Department"] == "HR"
    ]["Salary"].mean()
)

# Output:
# 75500.0

# Homework
print(df.sort_values("Name"))
# Output:
#     Name  Age Department  Salary
# 2   Amit   31         IT  82000
# 3   Neha   26    Finance  68000
# 4  Pooja   28         HR  76000
# 1  Rahul   28         HR  75000
# 5  Uday   30         IT  90000

print(df.sort_values("Salary", ascending=False))
# Output:
#     Name  Age Department  Salary
# 0   Uday   30         IT  90000
# 2   Amit   31         IT  82000
# 4  Pooja   28         HR  76000
# 1  Rahul   28         HR  75000
# 3   Neha   26    Finance  68000

print(df["Age"].value_counts())
# Output:
# 28    2
# 30    1
# 31    1
# 26    1

print(df["Department"].value_counts())
# Output:
# IT         2
# HR         2
# Finance    1

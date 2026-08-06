# Task 1

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Uday","Rahul","Amit","Neha"],
    "Age": [30, np.nan, 31, 26],
    "Salary": [90000,75000,np.nan,68000]
})

print(df)

# Task 2

print(df.isnull())
# Output:
#    Name    Age  Salary
# 0  False  False   False
# 1  False   True   False
# 2  False  False    True
# 3  False  False   False

print(df.isnull().sum())
# Output:
# Name      0
# Age       1
# Salary    1

# Task 3

print(df.dropna())
# Output:
#    Name   Age  Salary
# 0  Uday  30.0  90000.0
# 1  Neha  26.0  68000.0

# Task 4
print(df.fillna(0))

# Output:
#    Name   Age   Salary
# 0  Uday  30.0  90000.0
# 1  Rahul   0.0  75000.0
# 2  Amit  31.0      0.0
# 3  Neha  26.0  68000.0

# Task 5
df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print(df)

# Output:
#    Name   Age   Salary
# 0  Uday  30.0  90000.0
# 1  Rahul  29.0  75000.0
# 2  Amit  31.0  77666.666667
# 3  Neha  26.0  68000.0    

# Mentor Challenge 1
print(df["Age"].isnull().sum())
# Output:
# 0

# Mentor Challenge 2
print(df["Salary"].fillna(50000))

# Output:
# 0    90000.000000
# 1    75000.000000
# 2    77666.666667
# 3    68000.000000

# Mentor Mega Challenge
print(
    df.fillna(df.mean(numeric_only=True))
)

# Output:
#     Name   Age        Salary
# 0   Uday  30.0  90000.000000
# 1  Rahul  29.0  75000.000000
# 2   Amit  31.0  77666.666667
# 3   Neha  26.0  68000.000000

# Homework

df.isnull().sum()
# Output:
# Name      0
# Age       0
# Salary    0

df.fillna(100)
# Output:
#     Name   Age        Salary
# 0   Uday  30.0  90000.000000
# 1  Rahul  29.0  75000.000000
# 2   Amit  31.0  77666.666667
# 3   Neha  26.0  68000.000000

df.dropna()

# Output:
#     Name   Age        Salary
# 0   Uday  30.0  90000.000000
# 1  Rahul  29.0  75000.000000
# 2   Amit  31.0  77666.666667
# 3   Neha  26.0  68000.000000
# Task 1
import pandas as pd

df = pd.DataFrame({
    "Name": ["Uday", "Rahul", "Amit", "Neha", "Pooja"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [90000, 75000, 82000, 68000, 76000],
    "Age": [30, 28, 31, 26, 28]
})

print(
    df.groupby("Department")["Salary"].mean()
)
# Output:
# Department
# Finance    68000.0
# HR         75500.0
# IT         86000.0

# Task 2
print(
    df.groupby("Department")["Name"].count()
)
# Output:
# Department
# Finance    1
# HR         2
# IT         2

# Task 3
print(
    df.groupby("Department")["Salary"].max()
)
# Output:
# Department
# Finance    68000.0
# HR         76000.0
# IT         90000.0

print(
    df.groupby("Department")["Salary"].min()
)
# Output:
# Department
# Finance    68000.0
# HR         75000.0
# IT         82000.0

# Task 4
print(
    df.groupby("Department")["Salary"].agg(
        ["mean", "max", "min", "count"]
    )
)
# Output:
#            mean     max     min  count
# Department
# Finance  68000.0  68000.0  68000.0      1
# HR       75500.0  76000.0  75000.0      2
# IT       86000.0  90000.0  82000.0      2

# Mentor Challenge 1
print(
    df.groupby("Department")["Age"].mean()
)
# Output:
# Department
# Finance    26.0
# HR         28.0
# IT         30.5

# Mentor Challenge 2
print(
    df.groupby("Department")["Salary"].sum()
)
# Output:
# Department
# Finance     68000
# HR         151000
# IT         172000

# Mentor Mega Challenge
print(
    df.groupby("Department")[["Salary","Age"]].mean()
)
# Output:
#            Salary   Age
# Department
# Finance  68000.0  26.0
# HR       75500.0  28.0
# IT       86000.0  30.5

# Homework
print(
    df.groupby("Department")["Salary"].count()
)
# Output:
# Department
# Finance    1
# HR         2
# IT         2

print(
    df.groupby("Department")["Age"].max()
)
# Output:
# Department
# Finance    26.0
# HR         28.0
# IT         31.0

print(
    df.groupby("Department")["Age"].min()
)
# Output:
# Department
# Finance    26.0
# HR         28.0
# IT         30.0

print(
    df.groupby("Department")["Age"].agg(
        ["mean", "max", "min", "count"]
    )
)
# Output:
#            mean   max   min  count
# Department
# Finance  26.0  26.0  26.0     1
# HR       28.0  28.0  28.0     2
# IT       30.5  31.0  30.0    2
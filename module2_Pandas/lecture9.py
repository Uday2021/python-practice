# Task 1
import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Uday", "Rahul"],
    "Salary": [90000, 75000]
})

df2 = pd.DataFrame({
    "Name": ["Amit", "Neha"],
    "Salary": [82000, 68000]
})

print(pd.concat([df1, df2]))

# Output:
#     Name  Salary
# 0   Uday   90000
# 1  Rahul   75000
# 0   Amit   82000
# 1   Neha   68000

# Task 2
print(
    pd.concat(
        [df1, df2],
        ignore_index=True
    )
)
# Output:
#     Name  Salary
# 0   Uday   90000
# 1  Rahul   75000
# 2   Amit   82000
# 3   Neha   68000

# Task 3
df3 = pd.DataFrame({
    "Name": ["Uday", "Rahul"],
    "Age": [30, 28]
})

df4 = pd.DataFrame({
    "Salary": [90000, 75000],
    "City": ["Delhi", "Noida"]
})
print(
    pd.concat(
        [df3, df4],
        axis=1
    )
)

# Output:
#     Name  Age  Salary   City
# 0   Uday   30   90000  Delhi
# 1  Rahul   28   75000  Noida

# Mentor Challenge 1
print(
    pd.concat(
        [df1, df2],
        ignore_index=True
    ).shape
)

# Output:
# (4, 2)

# Mentor Challenge 2
print(
    pd.concat(
        [df3, df4],
        axis=1
    ).shape
)
# Output:
# (2, 4)

# Mentor Mega Challenge
df1 = pd.DataFrame({
    "Name": ["Uday", "Rahul"],
    "Age": [30, 28]
})

df2 = pd.DataFrame({
    "Name": ["Amit", "Neha"],
    "Salary": [82000, 68000]
})

result = pd.concat(
    [df1, df2],
    ignore_index=True
)

print(result)

# Output:
#   Name Age Salary
# 0 Uday 30  NaN
# 1 Rahul 28 NaN
# 2 Amit NaN 82000
# 3 Neha NaN 68000


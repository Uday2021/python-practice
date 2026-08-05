# Task 1

# csv created

# Task 2
import pandas as pd

df = pd.read_csv("./datasets/employee.csv")

print(df)

#    Name  Age  Salary
# 0   Uday   30   90000
# 1  Rahul   28   75000
# 2   Amit   31   82000
# 3   Neha   26   68000

print(df.head())

#     Name  Age  Salary
# 0   Uday   30   90000
# 1  Rahul   28   75000
# 2   Amit   31   82000
# 3   Neha   26   68000

print(df.tail(2))

#    Name  Age  Salary
# 2   Amit   31   82000
# 3   Neha   26   68000

print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4 entries, 0 to 3
# Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
# ---  ------  --------------  ----- 
#  0   Name    4 non-null      object
#  1   Age     4 non-null      int64 
#  2   Salary  4 non-null      int64 
# dtypes: int64(2), object(1)
# memory usage: 228.0+ bytes
# None

print(df.describe())

# Output:
#              Age       Salary
# count   4.000000      4.00000
# mean   28.750000  78750.00000
# std     2.217356   9429.56344
# min    26.000000  68000.00000
# 25%    27.500000  73250.00000
# 50%    29.000000  78500.00000
# 75%    30.250000  84000.0000０
# max    31.000000  90000.00000

# Mentor Challenge 1

print(df.shape)
# (4, 3)

# Mentor Challenge 2
print(df["Age"].mean())
# 28.75

# Mentor Mega Challenge

print(
    df[
        df["Salary"] > df["Salary"].mean()
    ][["Name","Salary"]]
)

# Output:
#     Name  Salary
# 0   Uday   90000
# 2   Amit   82000

# Homework

print(df["Salary"].max())
# 90000

print(df["Salary"].min())
# 68000

print(df["Age"].mean())
# 28.75

print(df["Age"].max())
# 31
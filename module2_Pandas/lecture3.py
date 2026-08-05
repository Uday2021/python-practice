# Task 1
#     Name   Age  Salary
# 0   Uday   30   90000
# 1  Rahul   28   75000
# 2   Amit   31   82000
# 3   Neha   26   68000

print(df.iloc[0])
# 0   Uday   30   90000

print(df.iloc[2])
# 2   Amit   31   82000

# Task 2
print(df.loc[1])
# 1  Rahul   28   75000
print(df.loc[3])
# 3   Neha   26   68000

# Task 3
print(df[df["Age"] > 28])
#     Name   Age  Salary
# 0   Uday   30   90000
# 2   Amit   31   82000

print(df[df["Salary"] > 70000])
#     Name   Age  Salary
# 0   Uday   30   90000
# 1  Rahul   28   75000
# 2   Amit   31   82000

# Task 4
print(
    df[
        (df["Age"] > 28)
        &
        (df["Salary"] > 80000)
    ]
)
#    Name   Age  Salary
# 0   Uday   30   90000
# 2   Amit   31   82000

# Mentor Challenge 1

print(df.iloc[1]["Name"])
# Rahul

# Mentor Challenge 2
print(
    df[df["Age"] < 30]["Name"]
)
# 1    Rahul
# 3     Neha

# Mentor Mega Challenge

print(
    df[
        (df["Age"] >= 30)
    ][["Name"]].shape
)
# (2, 1)

# Homework

print(df[(df["Age"] >= 30) & (df["Salary"] > 70000)][["Name", "Salary"]])
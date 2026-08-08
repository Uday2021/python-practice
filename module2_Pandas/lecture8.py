# Task 1

employees = pd.DataFrame({
    "EmpID": [1, 2, 3],
    "Name": ["Uday", "Rahul", "Amit"],
    "DeptID": [101, 102, 101]
})

departments = pd.DataFrame({
    "DeptID": [101, 102],
    "Department": ["IT", "HR"]
})

# Task 2
result = pd.merge(
    employees,
    departments,
    on="DeptID"
)

print(result)
# Output:
#    EmpID     Name  DeptID Department
# 0      1     Uday     101         IT
# 1      3     Amit     101         IT
# 2      2    Rahul     102         HR

# Task 3
print(
    pd.merge(
        employees,
        departments,
        on="DeptID",
        how="inner"
    )
)

# Output:
#    EmpID     Name  DeptID Department
# 0      1     Uday     101         IT
# 1      3     Amit     101         IT
# 2      2    Rahul     102         HR

# Mentor Challenge 1
print(
    pd.merge(
        employees,
        departments,
        on="DeptID"
    ).shape
)

# Output:
# (3, 4)

# Mentor Challenge 2
# Predict the Name column of the merged DataFrame.
print(
    pd.merge(
        employees,
        departments,
        on="DeptID"
    )["Name"]
)
# Output:
# 0     Uday
# 1     Amit
# 2    Rahul

# Mentor Mega Challenge
employees = pd.DataFrame({
    "EmpID": [1, 2, 3, 4],
    "Name": ["Uday", "Rahul", "Amit", "Neha"],
    "DeptID": [101, 102, 103, 101]
})

departments = pd.DataFrame({
    "DeptID": [101, 102],
    "Department": ["IT", "HR"]
})

result = pd.merge(
    employees,
    departments,
    on="DeptID"
)

print(result)

# Output:
#    EmpID   Name  DeptID Department
# 0      1   Uday     101         IT
# 1      4   Neha     101         IT
# 2      2  Rahul     102         HR
# 3      3   Amit     103         NaN
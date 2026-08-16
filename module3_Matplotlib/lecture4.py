# Task 1
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
    "Name": ["Uday", "Rahul", "Amit", "Neha", "Pooja"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [90000, 75000, 82000, 68000, 76000]
})

avg_salary = df.groupby("Department")["Salary"].mean()
avg_salary.plot(kind="bar")
plt.title("Department wise average salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.show()

# Department-wise Employee Count

emp_count = df["Department"].value_counts()
emp_count.plot(kind="bar")
plt.title("Department wise Employee count")
plt.xlabel("Department")
plt.ylabel("Employee count")

plt.show()

# Department-wise Maximum Salary

max_salary = df.groupby("Department")["Salary"].max()
max_salary.plot(kind="bar")
plt.title("Department wise Maximum salary")
plt.xlabel("Department")
plt.ylabel("Max Salary")

plt.show()

# Mentor Challenge 1
max_salary = df.groupby("Department")["Salary"].max()
# IT dept has highest average salary

# Mentor Challenge 2
# IT and HR has highest no. of employee 2.

# Mentor Challenge 3
# this question I do not understand what exactly want ?

# FINAL MEGA CHALLENGE
# Line chart we can use here and age is x-axis and salary y-axis








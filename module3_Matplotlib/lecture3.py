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

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.show()

# Task 2

count = df["Department"].value_counts()

count.plot(kind="bar")

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employee Count")

plt.show()

# Mentor Challenge 1
df.groupby("Department")["Salary"].mean()
# IT department rkhega highest

# Mentor Challenge 2
df["Department"].value_counts()
# Finance dept

# Mega Challenge
max_salary = df.groupby("Department")["Salary"].max()
max_salary.plot(kind="bar")

plt.title("Department wise max salary")
plt.xlabel("Department")
plt.ylabel("Max Salary")

plt.show()






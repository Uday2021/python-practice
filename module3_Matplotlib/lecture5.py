# Task 1

import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
    "Name": ["Uday", "Rahul", "Amit", "Neha", "Pooja"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Age": [ 30, 28, 29, 27, 25],
    "Salary": [90000, 75000, 82000, 68000, 76000]
})

avg_salary = df.groupby("Department")["Salary"].mean()
avg_salary.plot(kind="bar")
plt.title("Department wise Average salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.show()

employee_count = df["Department"].value_counts()
employee_count.plot(kind="bar")
plt.title("Department wise Employee count")
plt.xlabel("Department")
plt.ylabel("Employee Count")

plt.show()

age = [ 30, 28, 29, 27, 25]
salary = [90000, 75000, 82000, 68000, 76000]

plt.scatter(age, salary)

plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.show()


# Mentor Challenge
# IT
# 2
# 78200
# 90000
# Scatter

# Final Challenge
df.groupby("Department")["Salary"].mean().plot(kind="bar")
plt.show()






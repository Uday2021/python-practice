# Task 1

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 30]

plt.plot(x, y)

plt.title("Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

# Task 2

names = ["Uday", "Rahul", "Amit"]
salary = [90000, 75000, 82000]

plt.bar(names, salary)

plt.title("Employee Salary")
plt.xlabel("Employee")
plt.ylabel("Salary")

plt.show()

# Task 3

age = [25, 28, 30, 35, 40]
salary = [50000, 60000, 75000, 90000, 120000]

plt.scatter(age, salary)

plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.show()

# Task 4

ages = [20,22,22,25,25,25,28,30,30,35,40]

plt.hist(ages)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()

# Mentor Challenge 1

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)
# 5 points hone chahiye

# Mentor Challenge 2
# A - Bar chart
# B - Scatter chart



# Mentor Mega Challenge

department = ["IT", "HR", "Finance"]
employees = [20, 15, 8]

# Department-wise employee count ka chart banao.

# Answer:  Bar chart we can use here
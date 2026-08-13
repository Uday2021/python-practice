# Task 1
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 15, 30]
y1 = [10, 20, 15, 30]
y2 = [15, 18, 25, 35]

plt.figure(figsize=(8, 5))

plt.plot(
    x,
    y1,
    marker="o",
    linestyle="--",
    label="Product A"
)

plt.plot(
    x,
    y2,
    marker="o",
    linestyle="--",
    label="Product B"
)

plt.title("Sales Trend")
plt.grid()
plt.legend()

plt.show()


# Mentor Challenge 1
plt.plot(
    [1, 2, 3],
    [10, 20, 30],
    marker="o",
    linestyle="--"
)
# is graph me 3 markers honge

# Mentor Challenge 2
plt.plot(
    x,
    y,
    label="Revenue"
)

# graph pr Revenue nhi dikhayega

# Mentor Mega Challenge
months = ["Jan", "Feb", "Mar"]

product_a = [100, 150, 200]
product_b = [120, 140, 220]

# plt.plot hi use krenge using 3 variables and different lables. 
# label me product A and product B denge.
# plt.lagend method show krega.

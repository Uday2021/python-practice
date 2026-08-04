# Task 1

import numpy as np

arr = np.array([
    [10,20],
    [30,40]
])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))

# 100
# 25.0
# 40
# 10

# Task 2

print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))

# [40 60]
# [30 70]

# Task 3

print(np.mean(arr, axis=0))
print(np.mean(arr, axis=1))

# [20. 30.]
# [15. 35.]

# Mentor Challenge 1

import numpy as np

arr = np.array([
    [1,2],
    [3,4]
])

print(np.max(arr, axis=0))

# [3 4]

# Mentor Challenge 2

print(np.min(arr, axis=1))

# [1 3]

# Mentor Mega Challenge

import numpy as np

arr = np.array([
    [10,20,30],
    [40,50,60]
])

print(np.mean(arr[:,1]))

# 35.0

# Homework

arr = np.array([
    [5,10,15],
    [20,25,30],
    [35,40,45]
])

print(np.sum(arr))
# 225
print(np.sum(arr, axis=0))
# [60 75 90]
print(np.sum(arr, axis=1))
# [30 75 120]
print(np.mean(arr))
# 25.0
print(np.max(arr))
# 45
print(np.min(arr))
# 5
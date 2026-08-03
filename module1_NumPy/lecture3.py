import numpy as np

arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

# Task 1
print(arr[1])
print(arr[-1])

# [40 50 60]
# [70 80 90]

# Task 2
print(arr[:,1])
print(arr[:,2])

# [20 50 80]
# [30 60 90]

# Task 3
print(arr[0:2])
print(arr[:,0:2])

# [[10 20 30]
#  [40 50 60]]
# [[10 20]
#  [40 50]
# [70 80]]

# Mentor Challenge 1
print(arr[2,1])

# 80

# Mentor Challenge 2
print(arr[1:,1:])

# [[50 60]
#  [80 90]]

# Mentor Challenge 3 (Brain Twister)
print(arr[::-1,::-1])

# [[90 80 70]
#  [60 50 40]
#  [30 20 10]]


# Homework

arr = np.array([
 [1,2,3,4],
 [5,6,7,8],
 [9,10,11,12]
])

#Print:
# First row
print(arr[0])
# Last row
print(arr[-1])
# Second column
print(arr[:,1])
# Last two columns
print(arr[:,2:4])
# Bottom-right element
print(arr[-1,-1])
# Reverse rows
print(arr[::-1])
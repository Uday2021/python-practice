import numpy as np

a = np.array([1,2,3,4,5,6])

print(a.reshape(2,3))
print(a.reshape(3,2))

# [[1 2 3]
#  [4 5 6]]
# [[1 2]
#  [3 4]
#  [5 6]]

print(a.reshape(2,-1))
print(a.reshape(-1,2))

# [[1 2 3]
#  [4 5 6]]
# [[1 2]
#  [3 4]
#  [5 6]]

print(a.reshape(4,2))

# ValueError: cannot reshape array of size 6 into shape (4,2)


# Mentor Challenge 1

import numpy as np

a = np.array([10,20,30,40])

print(a.reshape(2,2))

# [[10 20]
#  [30 40]]

# Mentor Challenge 2
import numpy as np

a = np.array([1,2,3,4,5,6,7,8])

print(a.reshape(4,2))

# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# Mentor Mega Challenge
import numpy as np

a = np.array([1,2,3,4,5,6])

b = a.reshape(2,3)

print(b[1,2])

# 6

# Homework

a = np.array([10,20,30,40,50,60,70,80,90,100,110,120])

print(a.reshape(3,4))
# [[ 10  20  30  40]
#  [ 50  60  70  80]
#  [ 90 100 110 120]]

print(a.reshape(4,3))
# [[ 10  20  30]
#  [ 40  50  60]
#  [ 70  80  90]
#  [100 110 120]]

print(a.reshape(2,6))
# [[ 10  20  30  40  50  60]
#  [ 70  80  90 100 110 120]]

print(a.reshape(6,2))
# [[ 10  20]
#  [ 30  40]
#  [ 50  60]
#  [ 70  80]
#  [ 90 100]
#  [110 120]]

print(a.reshape(3,-1))
# [[ 10  20  30  40]
#  [ 50  60  70  80]
#  [ 90 100 110 120]]
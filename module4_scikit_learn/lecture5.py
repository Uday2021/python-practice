# Task 1

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import numpy as np

actual = [100, 200, 300]
predicted = [110, 190, 330]
mae = mean_absolute_error(actual, predicted)
mse = mean_squared_error(actual, predicted)
rmse = np.sqrt(mse)

print(mae)
print(mse)
print(rmse)


# Mentor Challenge 1
actual = [100, 200, 300]
predicted = [100, 200, 300]
# MSE - 0
# RMSE - 0
# MAE - 0


# Mentor Challenge 2
# Model A:
# MAE = 10
# RMSE = 12

# Model B:
# MAE = 8
# RMSE = 20

# Overall average error ke perspective se Model A better h
# large errors ki problem model B jyada show kr rha h

# Mega Challenge
# see average error me to model A is better and large error ki problem model B jyada show krega.

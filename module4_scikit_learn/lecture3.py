# Task 1
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
df = pd.DataFrame({
    "Experience": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Salary": [40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000]
})
X = df[["Experience"]]
y = df["Salary"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
# Task 2
model = LinearRegression()
model.fit(X_train, y_train)

# Task 3
y_pred = model.predict(X_test)

# Task 4
print(y_test)
print(y_pred)

# Task 5
score = r2_score(y_test, y_pred)
print(score)

# Mentor Challenge — Before Running
# 1. 4 rows
# 2. 1 row
# 3. X_train pr
# 4. test data pr
# 5. y_test means actual answer and y_pred means predicted output.



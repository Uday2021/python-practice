# Task
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [40000, 50000, 60000, 70000, 80000]
})

X = df[["Experience"]]
y = df["Salary"]

print(X)
print(y)

model = LinearRegression()

model.fit(X, y)

print(model.predict([[6]]))
print(model.predict([[10]]))

# Output
# [90000.]
# [130000.]

print(model.coef_)
print(model.intercept_)
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
poly = PolynomialFeatures(degree=2)

X = [[1], [2], [3], [4], [5]]
y = [3, 6, 11, 18, 27]

X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

print("X_poly:", X_poly)
print("Predictions:", model.predict(X_poly))

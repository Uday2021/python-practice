# Task 1
import pandas as pd
s = pd.Series(["A", "B", "A", "C", "B"])

mapping = {
    "A": "Apple",
    "B": "Banana",
    "C": "Cherry"
}

print(s.map(mapping))

# Apple, Banana, Apple, Cherry, Banana

# Task 2

s = pd.Series([10, 20, 30])

print(s.map(lambda x: x + 5))

# 15, 25, 35

# Mentor Challenge

df = pd.DataFrame({
    "Name": ["Uday", "Rahul", "Amit"],
    "Department": ["IT", "HR", "IT"]
})

mapping = {
    "IT": "Tech",
    "HR": "People"
}

df["Department"] = df["Department"].map(mapping)

print(df)

#  Name Department
# 0 Uday Tech
# 1 Rahul People
# 2 Amit Tech



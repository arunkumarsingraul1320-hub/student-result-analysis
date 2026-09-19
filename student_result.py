import pandas as pd
import matplotlib.pyplot as plt

# Student data
data = {
    "Name": ["Arun", "Rahul", "Amit", "Priya", "Neha"],
    "Maths": [78, 65, 55, 88, 72],
    "Python": [85, 70, 60, 92, 75],
    "DBMS": [80, 68, 58, 90, 70]
}

df = pd.DataFrame(data)

# Calculate total and average
df["Total"] = df["Maths"] + df["Python"] + df["DBMS"]
df["Average"] = df["Total"] / 3

# Pass / Fail
df["Result"] = df["Average"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

print("Student Result Analysis")
print(df)

# Average marks
print("\nAverage Marks:")
print(df[["Maths", "Python", "DBMS"]].mean())

# Bar chart
plt.bar(df["Name"], df["Average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Average Marks")
plt.show()
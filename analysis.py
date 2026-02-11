import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")
print(df.head())

avg = df.groupby("Subject")["Marks"].mean()
avg.plot(kind="bar")
plt.show()

plt.scatter(df["Attendance"], df["Marks"])
plt.show()

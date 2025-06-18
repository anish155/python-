import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('space.csv')

print(df)

outcome_counts = df["Outcome"].value_counts()

plt.title("Mission Result")
plt.bar(outcome_counts.index, outcome_counts.values, color=['green', 'orange', 'blue'])
plt.xlabel("Outcome")
plt.ylabel("Number of Missions")
plt.tight_layout()
plt.show()


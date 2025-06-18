import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('space.csv')

outcome_counts = df["Outcome"].value_counts()

plt.pie(outcome_counts, labels=outcome_counts.index, autopct='%1.1f%%', colors=['green', 'orange', 'blue'])
plt.title("Mission Outcomes Distribution")
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sale=np.array([[2023,"Anish Tandukar","bachelor",20,13000],
               [2023, "Ramesh Shrestha", "bachelor", 22, 14500],
               [2023, "Sunita Karki", "bachelor", 21, 14000],

               [2024,"Anish Tandukar","master",23,35000],
               [2024, "Ramesh Shrestha", "master", 26, 36000],
               [2024, "Sunita Karki", "master", 24, 34000],

               [2025,"Anish Tandukar","master",24,39000],
               [2025, "Ramesh Shrestha", "phd", 30, 40000],
               [2025, "Sunita Karki", "phd", 32, 42000]
               ],dtype=object)

df=pd.DataFrame(sale,columns=["Year","Name","Education","Age","Salary"])
print("2023's salary data")
print(df[df["Year"]==2023])
print("2024's salary data")
print(df[df["Year"]==2024])
print("2025's salary data")
print(df[df["Year"]==2025])

pivot_df = df.pivot(index="Name", columns="Year", values="Salary")
pivot_df.plot(kind="bar",figsize=(10,6))
plt.title("Salary")
plt.xlabel('Name')
plt.ylabel('salary(NPR)')
plt.xticks(rotation=45)
plt.legend(title="Year")
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
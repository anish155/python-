import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("bank.csv")
print(df.head())

plt.figure(figsize=(10,5))
plt.plot(df["High"], label="High", color="red")
plt.plot(df["Low"], label="Low", color="blue")

plt.title("stock")
plt.xlabel("rate")
plt.ylabel("frequency")
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()
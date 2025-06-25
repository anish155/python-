import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Cancer.csv")

print(df.head(20))

grouped=df.groupby(["Gender","Age"]).size().reset_index(name="Count")

top=grouped.sort_values(by="Count",ascending=False).head(5)

plt.figure(figsize=(8,5))
sns.barplot(data=top, x="Gender", y="Count", hue="Age", dodge=True)

plt.title("which gender of what age suffers most from cancer!")
plt.xlabel("gender")
plt.ylabel("age")
plt.tight_layout()
plt.show()
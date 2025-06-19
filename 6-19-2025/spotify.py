import pandas as pd
import matplotlib.pyplot as plt
import random

df=pd.read_csv('artists.csv')

print(df.head())

top_50 = df.sort_values(by='popularity', ascending=False).head(50)

colors=['#%06X' % random.randint(0, 0xFFFFFF) for _ in range(len(top_50))]

plt.figure(figsize=(16,8))
plt.bar(top_50['name'], top_50['popularity'], color=colors)
plt.title("popularity of top 50 artist")
plt.xlabel("artist")
plt.ylabel("popularity")
plt.xticks(rotation=60)
plt.tight_layout()
plt.show()
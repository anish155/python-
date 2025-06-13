import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('movie.csv')
plt.title('Ratings')
plt.xlabel('Movies')
plt.ylabel('rates')
plt.bar(df['Title'],df['Rating'])
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
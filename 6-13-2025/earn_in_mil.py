import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('movie.csv')
plt.title('movie earning')
plt.pie(df['BoxOfficeMillions'],labels=df['Title'])
plt.show()
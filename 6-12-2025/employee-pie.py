import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('employee.csv')

plt.pie(df['Salary'],labels=df['Name'])
plt.title("earning")
plt.legend(loc='upper right')
plt.show()
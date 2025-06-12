import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('employee.csv')

plt.title('salary')
plt.xlabel('name')
plt.ylabel('earn')
plt.plot(df['Name'],df['Salary'], marker='o', linestyle='-', color='blue', label='Data Points')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()
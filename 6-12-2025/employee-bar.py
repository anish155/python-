import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('C:/Users/user/OneDrive/Desktop/python/6-12(Thrusday)/employee.csv')
print(df)

plt.figure(figsize=(10, 6)) 
plt.bar(df['Name'],df['Salary'],color='skyblue')

plt.title("Employee-Salary")
plt.xlabel('employee')
plt.ylabel('salary')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()   
plt.show()
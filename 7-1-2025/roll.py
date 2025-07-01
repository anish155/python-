import pandas as pd
df=pd.read_csv("student.csv")
roll=pd.DataFrame(df["Age"])
print(roll)
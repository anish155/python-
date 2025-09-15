import numpy as np
import pandas as pd


data=np.array(["Anish","The Jungle Book","Cheese Cake"])
print(data)

table=pd.DataFrame(data)
print(table)

name=pd.DataFrame([data[0]],columns=["Name"])
print(name)


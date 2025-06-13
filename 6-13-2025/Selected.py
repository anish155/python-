import pandas as pd
from tabulate import tabulate as tb
df=pd.read_csv('movie.csv')
selected=df[['Title','Genre','Rating']]
print(tb(selected,headers='keys',tablefmt='pipe'))
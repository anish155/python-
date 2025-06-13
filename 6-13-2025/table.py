import pandas as pd
from tabulate import tabulate as tb
df=pd.read_csv('movie.csv')

print(tb(df,headers='keys',tablefmt='grid'))

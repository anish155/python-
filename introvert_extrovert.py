import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('personality_dataset.csv')
print(df.head())

stage_fear_counts = df.groupby(['Personality', 'Stage_fear']).size().unstack()

stage_fear_counts.plot(kind='bar')

plt.title("kon banega karod pati")
plt.xlabel("personality")
plt.ylabel("Stage_fear")
plt.legend(title='Stage Fear')
plt.tight_layout()
plt.show()
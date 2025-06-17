import matplotlib.pyplot as plt

activities=['Sleep', 'Classes', 'Homework/Study', 'Social Media', 'Gaming', 'Exercise', 'Eating', 'Leisure/TV']
hours=[7, 5, 4, 2, 1, 1, 2, 2]

plt.figure(figsize=(8,8))
plt.pie(hours,labels=activities,autopct='%1.1f%%', startangle=140)
plt.title("student schedule")
plt.tight_layout()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

person = {
    "name": "Anish Tandukar",
    "age": 20,
    "city": "Kathmandu",
    "work": "Coding"
}
ages = {
    "Anish": 20,
    "Bikash": 22,
    "Sita": 19,
    "Hari": 25
}

df = pd.DataFrame([person]) 
print(df)

plt.bar(ages.keys(), ages.values(), color='skyblue')
plt.xlabel("Names")
plt.ylabel("Age")
plt.title("Ages of People")
plt.show()

df = pd.DataFrame(list(ages.items()), columns=["Name", "Age"])

sb.barplot(x="Name", y="Age", data=df)
plt.title("Ages of People")
plt.show()
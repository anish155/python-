import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

name=np.array([("Anish",20,"backelor","bsc hons comp",0),
               ("kamlesh",26,"graduated","Bscit",50000),
               ("Riya", 22, "Bachelor", "BSc CS", 10000),
               ("Sita", 23, "Graduated", "BCA", 30000),
               ("Ram", 25, "Postgrad", "MSc CS", 60000),
               ("Laxmi", 21, "Bachelor", "BSc IT", 15000)],dtype=object)
print(name)

df=pd.DataFrame(name,columns=["Name", "Age", "Education", "Course", "Salary"])
print(df)

# Plotting salary by name
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Salary"], color="skyblue")
plt.title("Salary of Individuals")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

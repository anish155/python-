import pandas as pd
import matplotlib.pyplot as plt
person={"name":["anish","rahul","dinesh","pujan","hari","kamal"],
        "age":[20,15,14,19,25,30],
        "job":["frontend","database","backend","designer","frontend","designer"],
        "Salary":[20000,18000,21000,15000,19000,15000]}
df=pd.DataFrame(person)

plt.title("Work Data")
plt.xlabel("employees")
plt.ylabel("salary")
plt.bar(person["name"],person["Salary"])
plt.show()
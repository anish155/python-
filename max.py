dic={"id":10001,
     "age":20}
max_key=None
max_value=0
for i in dic:
        if dic[i]>max_value:
            max_value=dic[i]
            max_key=i
print(max_key)


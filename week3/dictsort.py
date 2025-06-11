person={"anish":20,"rajib":25,"koirala":14}
lis=list(person.keys())
lis.sort()

result={i:person[i]for i in lis}
print(result)



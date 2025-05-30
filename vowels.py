sentence=input("enter the word:")
count=0
for x in sentence:
    #if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
    if x in 'aeiou':
        count+=1
print(count)


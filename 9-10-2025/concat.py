cat=["Tiger","Panther"]
growl=["rawr","purr"]

species=input("Enter the cat species:")

for i in range(len(cat)):
    if species == cat[i]:
        print("Growl",growl[i])
        break
    else:
        print("An unknown cat has apperead.") 
def add_contact():
    individuals=int(input("Enter the number of individual contacts your want to store:"))
    contact_dict={}
    for _ in range(individuals):
        print("Creating user data:")
        name=input("Enter users name:")
        address=input("Enter users address:")
        phone=int(input("Enter users phone number:"))
        email=input("Enter users E-mail:")
        contact_dict[name]=[address,phone,email]
        
    return contact_dict

def store(contact_dict):
    print("contact info:")
    for name,details in contact_dict.items():
        print(f"Name: {name}")
        print(f"Address: {details[0]}")
        print(f"Phone: {details[1]}")
        print(f"Email: {details[2]}")
        print()

def find(contact_dict):
    print("Finding the individual:")
    indi_name=input("Enter the name of person that you want to find:")
    if indi_name in contact_dict:
        details=contact_dict[indi_name]
        print(f"Address: {details[0]}")
        print(f"Phone: {details[1]}")
        print(f"Email: {details[2]}")
    else:
        print("person not found.")
        
def removing(contact_dict):
    print("Removing the indivisual:")
    indi_rmn=input("Enter the individual you want to remove:")
    if indi_rmn in contact_dict:
        del contact_dict[indi_rmn]
        print(f"{indi_rmn} details removed.")
    else:
        print("person not found.")

while True:
    option=int(input("Enter the option you want:"))
    if option ==1:
        contact=add_contact()
    elif option==2:
        store(contact)
    elif option ==3:
        find(contact)
    elif option==4:
        removing(contact)
    elif option==5:
        print("Exiting the program")
        break
    else:
        print("Wrong option, Try again.")


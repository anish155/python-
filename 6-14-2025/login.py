print("Home page")
print("1. if account exists(Log in)")
print("2. if no account(Sign up)")
option=int(input("Enter according to your need (1 or 2):"))
if option==1:
    print("Login Panel")
    username=input("Enter the username:")
    password=input("Enter the password:")
    found=False
    with open("C:/Users/user/OneDrive/Desktop/python/6-14-2025/User.txt","r") as file:
        for line in file:
            cred=line.strip().split(",")
            if len(cred) >= 5:
                file_username = cred[2]
                file_password = cred[4]
                if file_username == username and file_password == password:
                    found = True
                    break
    if found:
        print("Login successful!")
    else:
        print("Login failed. Invalid username or password.")


elif option==2:
    print("Signup Panel")
    firstname=input("Enter the user firstname:")
    lastname=input("Enter the user lastname:")
    username=input("Enter the username:")
    email=input("Enter the user email:")
    password=input("Enter the password:")

    with open("C:/Users/user/OneDrive/Desktop/python/6-14-2025/User.txt", "a") as file:
        file.write(f"{firstname},{lastname},{username},{email},{password}\n")

    print("Signup successful! You can now log in.")

else:
    print("Invalid option. Please enter 1 or 2.")
    
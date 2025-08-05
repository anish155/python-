def login():
    test=[{"username":"anish",
           "password":"anish123"},
           {"username":"tester",
            "password":"default"}]
    username=input("Enter the username:")
    password=input("Enter the password:")
    
    def config():
        for users in test:
            if users["username"]==username and users["password"]==password:
                 print("Login successful!")
                 print(f"Welcome, {username}")
                 return True
        print("Invalid credentials.")
        return False
    config()

login()
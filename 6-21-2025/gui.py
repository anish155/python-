import tkinter as tk

def submit_form():
    fname = e1.get()
    lname = e2.get()
    gender = gender_var.get()
    country = country_var.get()
    newsletter = newsletter_var.get()

    print("Submitted Info:")
    print("First Name:", fname)
    print("Last Name:", lname)
    print("Gender:", gender)
    print("Country:", country)
    print("Newsletter Subscription:", "Yes" if newsletter else "No")

def open_form():
    new_window = tk.Toplevel(m)
    new_window.title("Form Page")
    new_window.geometry("400x300")  # Set window size

    # First Name and Last Name
    tk.Label(new_window, text="First Name").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    tk.Label(new_window, text="Last Name").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    global e1, e2
    e1 = tk.Entry(new_window)
    e2 = tk.Entry(new_window)
    e1.grid(row=0, column=1, padx=10)
    e2.grid(row=1, column=1, padx=10)

    # Gender (Radio Buttons)
    tk.Label(new_window, text="Gender").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    global gender_var
    gender_var = tk.StringVar()
    tk.Radiobutton(new_window, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky="w")
    tk.Radiobutton(new_window, text="Female", variable=gender_var, value="Female").grid(row=2, column=1)

    # Country (Dropdown Menu)
    tk.Label(new_window, text="Country").grid(row=3, column=0, sticky="w", padx=10, pady=5)
    global country_var
    country_var = tk.StringVar(value="Select")
    countries = ["Nepal", "India", "USA", "UK"]
    tk.OptionMenu(new_window, country_var, *countries).grid(row=3, column=1, padx=10)

    # Newsletter Subscription (Checkbox)
    global newsletter_var
    newsletter_var = tk.IntVar()
    tk.Checkbutton(new_window, text="Subscribe to newsletter", variable=newsletter_var).grid(row=4, columnspan=2, pady=5)

    # Submit Button
    tk.Button(new_window, text="Submit", command=submit_form).grid(row=5, columnspan=2, pady=10)

# Main window
m = tk.Tk()
m.title("Main Window")
m.geometry("300x150")

tk.Button(m, text="Open Form", width=25, command=open_form).pack(pady=40)

m.mainloop()

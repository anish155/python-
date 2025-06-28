import tkinter as tk
main=tk.Tk()
main.title("Login form")
main.geometry("500x300")
main.config(bg="light blue")

username_label=tk.Label(main,text="Username",font=('calibre',10, 'bold'))
username_field=tk.Entry(main,textvariable=tk.StringVar(),font=('calibre',10, 'normal'))

password_label=tk.Label(main,text="Password",font=('calibre',10, 'bold'))
password_field=tk.Entry(main,textvariable=tk.StringVar(),font=('calibre',10, 'normal'))

button=tk.Button(main,text="Submit",command= "submit")

username_label.grid(row=0,column=0)
username_field.grid(row=0,column=1)
password_label.grid(row=1,column=0)
password_field.grid(row=1,column=1)
button.grid(row=2,column=1)

main.mainloop()
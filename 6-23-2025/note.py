import tkinter as tk
from tkinter import filedialog as fd
def save_file():
    file_path=fd.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files","*.txt"),("All files","*.*")],
        title="save your notes"
    )
    if file_path:
        content=txtarea.get("1.0","end-1c")
        with open(file_path,"w",encoding="utf-8") as file:
            file.write(content)

m=tk.Tk()
m.title("notes")
m.geometry("700x550")
txtarea=tk.Text(m,height = 27,
                width = 70,
                bg = "light yellow")
button=tk.Button(m, 
                   text="Save", 
                   command=save_file,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)
txtarea.pack(pady=(50,0))
button.pack(padx=10,pady=20)
tk.mainloop()
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def action():
    n1 = float(e1.get())
    n2 = float(e2.get())
    rs = n1+n2
    e3.insert(0, n1)
    messagebox.showinfo("Message", "Addition is : "+str(rs))
    messagebox.showinfo("Message", "Cur : "+cb1.get())
root = tk.Tk()
root.geometry("600x400")
e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)
btn = tk.Button(root, text="CLICK", command=action)
cities = ["Udaipur", "Jaipur", "Udaipur"]
cb1 = ttk.Combobox(root, values=cities, state='readonly')
cb1.current(1)
e1.pack()
e2.pack()
e3.pack()
btn.pack()
cb1.pack()

# def action(event):
#     'to call'
#     tk.messagebox("INFO", "Hello")
# cb1.bind("<<ComboboxSelected>>", action(self))
root.mainloop()

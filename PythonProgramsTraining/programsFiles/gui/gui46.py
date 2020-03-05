import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def click():
    'to perform action on button click'
    n1 = float(tf1.get())
    n2 = float(tf2.get())
    # getting current item from combobox
    item = cb1.get()
    if item=="+":
        rs = n1+n2
        messagebox.showinfo("MessageBox", "Addition is : "+str(rs))
    elif item=="-":
        rs = n1-n2
        messagebox.showinfo("MessageBox", "Subtraction is : "+str(rs))
    elif item=="x":
        rs = n1*n2
        messagebox.showinfo("MessageBox", "Product is : "+str(rs))
    elif item=="/":
        rs = n1/n2
        messagebox.showinfo("MessageBox", "Division is : "+str(rs))
    else:
        messagebox.showinfo("MessageBox", "select an action")
    # setting result into TextField
    tf3.insert(0, rs)
# creating a frame
root = tk.Tk()
# setting frame size
root.geometry("600x400")
# creating TextField
tf1 = tk.Entry(root)
tf2 = tk.Entry(root)
tf3 = tk.Entry(root)
# creating Button
btn = tk.Button(root, text="CLICK", command=click)
ls = ['Select Action', '+', '-', 'x', '/']
# creating ComboBox
cb1 = ttk.Combobox(root, values=ls, state='readonly')
cb1.current(0)
# adding Controls over frame
cb1.pack()
tf1.pack()
tf2.pack()
tf3.pack()
btn.pack()
# showing frame
root.mainloop()





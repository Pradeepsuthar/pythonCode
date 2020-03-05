import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def operation():
    'to execute task on button click'
    item = cb.get()
    messagebox.showwarning("WARNING", item+" is Selected")

root = tk.Tk()
root.geometry("600x400")

city = ["Udaipur", 'Jaipur', "Jodhpur"]
# creating ComboBox
cb = ttk.Combobox(root, values=city, state="readonly")
cb.current(0)
btn = tk.Button(root, text="CLICK", command=operation)
cb.pack()
btn.pack()
root.mainloop()
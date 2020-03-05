import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("600x400")
v = StringVal()
def sel():
    messagebox.showinfo("Selected")
rbtnM = tk.Radiobutton(root, text="Male", value="Male", command=sel)
rbtnF = tk.Radiobutton(root, text="Female", value="Female", command=sel)
rbtnM.pack()
rbtnF.pack()
root.mainloop()
import tkinter as tk
import tkinter as tkk
from tkinter import messagebox

def operation():
    item = cb.get()
    messagebox.showwarning("Warning", item+" is selected")
    
# creating a frame
frame = tk.Tk()
frame.geometry("200x200")
city = ["Udaipur", "Jaipur", "Jodhapur"]
#Creating controls
cb = tkk.Combobox(root, values=city, state="readonly")
cb.current(0)
btn = tk.Button(frame, text="Click", command=operation)
# Adding components on frame
btn.pack()
# Showing frame
frame.mainloop()
import tkinter as tk
from tkinter import messagebox
def area():
    'to calculate area'
    len = float(tfLen.get())
    wid = float(tfWidth.get())
    result = len*wid
    tfArea.insert(0,result)
    # Showing massage box
    messagebox.showinfo("Info MAss ", "Area is : "+str(result)+" CM")


# creating a frame
frame = tk.Tk()
frame.geometry("200x200")
#Creating controls
tfLen = tk.Entry(frame)
tfWidth = tk.Entry(frame)
tfArea = tk.Entry(frame)
btn = tk.Button(frame, text="Calculate Area", command=area)
# Adding components on frame
tfLen.pack()
tfWidth.pack()
tfArea.pack()
btn.pack()
# Showing frame
frame.mainloop()
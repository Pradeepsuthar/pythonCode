import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")

def bar():
    import time
    pbar["value"] = 50
    pbar.update_idletasks()
    time.sleep(2)
    pbar["value"] = 100
    pbar.update_idletasks()
    time.sleep(2)
    pbar["value"] = 150
    pbar.update_idletasks()
    time.sleep(2)
    pbar["value"] = 200
    pbar.update_idletasks()
    time.sleep(2)
    pbar["value"] = 300
    pbar.update_idletasks()
    time.sleep(2)
    pbar["value"] = 300
    pbar.update_idletasks()

pbar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
btn = tk.Button(root, text="Start", command=bar)
pbar.pack()
btn.pack()
root.mainloop()



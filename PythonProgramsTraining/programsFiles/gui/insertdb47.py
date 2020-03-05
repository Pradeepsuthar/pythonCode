import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

frame = tk.Tk()
frame.geometry("600x400")

def insert():
    'to insert into db'
    an = tfANo.get()
    ahn = tfAHName.get()
    ab = tfAB.get()
    doa = tfDOA.get()
    city = cbCity.get()
    # connect db
    con = mysql.connector.connect(host="localhost",port="3306",
        user="root",passwd="aptech",database="gits47")
    trolley = con.cursor()
    sql="insert into accountmaster values\
        ("+an+",'"+ahn+"',"+ab+",'"+doa+"','"+city+"');"
    trolley.execute(sql)
    con.commit()
    if trolley.rowcount>0:
        messagebox.showinfo("INFO", "Wow! Data Inserted")
    else:
        messagebox.showinfo("INFO", "Data did not Inserted")
    trolley.close()
    con.close()

# creating controls
tfANo = tk.Entry(frame)
tfAHName = tk.Entry(frame)
tfAB = tk.Entry(frame)
tfDOA = tk.Entry(frame)
city=["Jaipur","Jodhpur","Udaipur","Ajmer"]
cbCity = ttk.Combobox(frame, values=city, state='readonly')
cbCity.current(0)
btn = tk.Button(frame, text="SUBMIT", command=insert)
# adding on frame
tfANo.pack()
tfAHName.pack()
tfAB.pack()
tfDOA.pack()
cbCity.pack()
btn.pack()
frame.mainloop()
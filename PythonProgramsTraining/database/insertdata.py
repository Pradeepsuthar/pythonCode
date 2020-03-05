import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

frame = tk.Tk()
frame.geometry("600x400")

def insert():
    'to insert into db'
    an = tfANo.get()
    ahn = tfAName.get()
    ab = tfAB.get()
    doa = tfDOA.get()
    city = cbCity.get()
    # connect db
    con = mysql.connector.connect(host="localhost",port="3306",user="root",passwd="",database="gits079")
    trolly = con.cursor()
    sql = "insert into accountmaster values("+no+",'"+name+"',"+bal+",'"+date+"','"+city+"');"
    cursor.execute(sql)
    #commiting sql
    con.commit()
    if trolly.rowcount>0:
        messagebox.showinfo("INFO", "Data inserted")
    else:
        messagebox.showinfo("INFO", "Data Not inserted")
    trolly.close()
    con.close()

# Creating controls
tfANo = tk.Entry(frame)
tfAName = tk.Entry(frame)
tfAB = tk.Entry(frame)
tfDOA = tk.Entry(frame)
city = ["Udaipur","Jaipur","Kota"]
cbCity = tk.Combobox(frame, values=city, state="readonly")
cbCity.current(0)
btn = tk.Button(frame, text="Submit", command=insert)
# adding on frame
tfANo.pack()
tfAName.pack()
tfAB.pack()
tfDOA.pack()
cbCity.pack()
btn.pack()
frame.mainloop()

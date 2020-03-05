from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

frame = tk.Tk()
frame.title("Insert Data in DB")
frame.geometry('300x160')

def insert():
    'to insert into db'
    an = tfANo.get()
    ahn = tfAName.get()
    ab = tfAB.get()
    doa = tfDOA.get()
    city = cbCity.get()
    # connection
    con = mysql.connector.connect(host="localhost",port="3306",user="root",passwd="",database="gits079")
    trolly = con.cursor()
    sql = "insert into accountmaster values("+an+",'"+ahn+"',"+ab+",'"+doa+"','"+city+"');"
    trolly.execute(sql)
    #commiting sql
    con.commit()
    if trolly.rowcount>0:
        messagebox.showinfo("INFO", "Data inserted")
    else:
        messagebox.showinfo("INFO", "Data Not inserted")
    trolly.close()
    con.close()

# Creating controls

l1=Label(frame,text="Account No.",fg = "black",font = "Times")
l1.grid(row=0,column=0)
tfANo = tk.Entry(frame)
tfANo.grid(row=0,column=1)

l2=Label(frame,text="Account Holder Name",fg = "black",font = "Times")
l2.grid(row=1,column=0)
tfAName = tk.Entry(frame)
tfAName.grid(row=1,column=1)

l3=Label(frame,text="Account Balance",fg = "black",font = "Times")
l3.grid(row=2,column=0)
tfAB = tk.Entry(frame)
tfAB.grid(row=2,column=1)

l4=Label(frame,text="DOA",fg = "black",font = "Times")
l4.grid(row=3,column=0)
tfDOA = tk.Entry(frame)
tfDOA.grid(row=3,column=1)

l5=Label(frame,text="City",fg = "black",font = "Times")
l5.grid(row=4,column=0)
city = ["Udaipur","Jaipur","Kota"]
cbCity = ttk.Combobox(frame, values=city, state="readonly")
cbCity.current(0)
cbCity.grid(row=4,column=1)

btn = tk.Button(frame, text="Submit", command=insert)
btn.grid(row=5,column=0)
frame.mainloop()
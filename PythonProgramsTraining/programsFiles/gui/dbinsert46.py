import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

frame = tk.Tk()
frame.geometry("600x400")

def insert():
    'to insert into empmaster'
    try:
        ec = tfEC.get()
        en = tfEN.get()
        es = tfES.get()
        edob = tfEDOB.get()
        ecity = cbCity.get()
        # db connection
        con = mysql.connector.connect(host="localhost",port="3306",
            user="root",passwd="aptech",database="gits46")
        if con:
            print("DB Connected")
        cursor = con.cursor()
        sql = "insert into empmaster values\
             ("+ec+", '"+en+"', "+es+", '"+edob+"', '"+ecity+"');"
        cursor.execute(sql)
        if cursor.rowcount==1:
            messagebox.showinfo("INFO", "Data inserted")
        else:
            messagebox.showinfo("INFO", "Data did not inserted")
        con.commit()
        cursor.close()
        con.close()
    except Exception as ex:
        messagebox.showinfo("INFO", str(ex) )

tfEC = tk.Entry(frame)
tfEN = tk.Entry(frame)
tfES = tk.Entry(frame)
tfEDOB = tk.Entry(frame)
cbCity = ttk.Combobox(frame,
        values=["Jaipur","Udaipur","Ajmer","jodhpur"])
cbCity.current(0)
btn = tk.Button(frame, text="SUBMIT", command=insert)
tfEC.pack()
tfEN.pack()
tfES.pack()
tfEDOB.pack()
cbCity.pack()
btn.pack()
frame.mainloop()
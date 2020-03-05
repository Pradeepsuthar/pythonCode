from tkinter import *
import tkinter as tk
from tkinter import ttk
import json

FILE_NAME = "data.json"
fr = open(FILE_NAME)
# reading all data from json file info python compative
data = json.load(fr)
fr.close()

# print("*"*120)
# print("Flight No.\tFrom\tTo\tAirport Name\t\t\tTime\tFlight\t\t\tPrice\t\t")
# print("*"*120)
# print("%s\t\t%s\t%s\t%s\t\t\t%s\t%s\t\t\tRs.%0.2f\t\t"\
#     %(data[item]["flightNum"],data[item]["fromCode"],data[item]["toCode"],data[item]["AirportName"],data[item]["time"],data[item]["type"],float(data[item]["price"])))

def find_flight():
    var_boarding  = boarding.get()
    var_destination  = destination.get()

    for item in data:
        if data[item]["fromCode"] == var_boarding and data[item]["toCode"] == var_destination:
            print("Flight No. : %s"%(data[item]["flightNum"]))
            print("From : %s"%(data[item]["fromCode"].title()))
            print("To : %s"%(data[item]["toCode"].title()))
            print("Airport Name : %s"%(data[item]["AirportName"].title()))
            print("Time : %s"%(data[item]["time"]))
            print("Flight : %s"%(data[item]["type"].title()))
            print("Price : Rs.%0.2f"%(float(data[item]["price"])))
            print("*"*120)
        else:
            print("Data Not found")


win=Tk()
win.title("Insert Data in DB")
win.geometry('300x160')

l1=Label(win,text="Enter your route -",fg = "Red",font = "Times")
l1.grid(row=0,column=0)

l2=Label(win,text="From :",fg = "black",font = "Times")
l2.grid(row=1,column=0)
boarding = tk.Entry(win)
boarding.grid(row=1,column=1)

l3=Label(win,text="Destination :",fg = "black",font = "Times")
l3.grid(row=2,column=0)
destination = tk.Entry(win)
destination.grid(row=2,column=1)

l4=Label(win,text="City",fg = "black",font = "Times")
l4.grid(row=4,column=0)
travel_class  = ["Economy","Business","First Class","Premium Economy"]
travel_class  = ttk.Combobox(win, values=travel_class , state="readonly")
travel_class .current(0)
travel_class .grid(row=4,column=1)

btn = tk.Button(win, text="Search Flight", command=find_flight)
btn.grid(row=5,column=1)

win.mainloop()
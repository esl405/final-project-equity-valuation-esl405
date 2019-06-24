import tkinter
import pandas
import os
from tkinter import *
#can import finviz

#User Input and Input GUI
root=Tk()
root.title("Please Input the Following Parameters:")
root.geometry("500x500")
#pps =Button(root, text='Rock',command=lambda:[click_button("Rock"), new_window()]).pack(side=LEFT, anchor=W)
pps_text=Label(root, text='Price Per Share: ').grid(row=0, column=1)
pps=Entry(root).grid(row=0, column=2)
shares_outstanding_text=Label(root, text='Shares Outstanding (Millions): ').grid(row=1, column=1)
shares_outstanding=Entry(root).grid(row=1, column=2)
debt_text=Label(root, text='Market Value or Book Value of Debt ($M): ').grid(row=2, column=1)
debt=Entry(root).grid(row=2, column=2)
risk_free_rate_text=Label(root, text='Shares Outstanding: ').grid(row=3, column=1)
risk_free_rate=Entry(root).grid(row=3, column=2)

root.mainloop()


#def new_window():
#    top=Toplevel()
#    top.title("Please Input the Following Parameters: ")
#    top.geometry("300x200")
#    line1=Label(top, Text="User Choice: ") #confirm
#    top.mainloop()

#print (line1)









#Calculations


#Output GUI
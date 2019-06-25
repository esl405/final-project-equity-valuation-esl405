import tkinter
import pandas
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
#can import finviz

#User Input and Input GUI
#debt_text=Label(root, text='Market Value or Book Value of Debt ($M): ').grid(row=2, column=1)
#debt=Entry(root).grid(row=2, column=2)
#risk_free_rate_text=Label(root, text='Shares Outstanding: ').grid(row=3, column=1)
#risk_free_rate=Entry(root).grid(row=3, column=2)
#
#
#Button(root, text='Done',command=root.quit, fg='red').grid(row=10, column=2)
#
#root.mainloop()

#from https://www.sololearn.com/Discuss/501434/need-example-for-get-values-from-textbox-tkinter

class MainFrame(ttk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()

        
        
    def create_widgets(self):
                       
        self.pps_text = ttk.Label(text='Price per Share: ')
        self.pps_text.grid(column=1,row=0)


        self.pps = tk.Entry()
        self.pps.grid(column=2,row=0)

        self.shares_outstanding_text = ttk.Label(text='Shares Outstanding: ')
        self.shares_outstanding_text.grid(column=1,row=1)

        self.shares_outstanding = tk.Entry()
        self.shares_outstanding.grid(column=2,row=1)

        self.debt_text = ttk.Label(text='Market or Book Value of Debt ($M): ')
        self.debt_text.grid(column=1,row=3)

        self.debt = tk.Entry()
        self.debt.grid(column=2,row=3)

        self.rrf_text = ttk.Label(text='Risk Free Rate (%): ')
        self.rrf_text.grid(column=1,row=4)

        self.rrf = tk.Entry()
        self.rrf.grid(column=2,row=4)




        self.label1 = tk.Label(text="default text")
        self.label1.grid(column=3,row=0)

        self.label2 = tk.Label(text="default text")
        self.label2.grid(column=3,row=1)

        self.button1 = ttk.Button(text='confirm inputs', command=self.write)
        self.button1.grid(column=1,row=4)

    def write(self):
        self.label1["text"]=self.pps.get()
        self.label2["text"]=self.shares_outstanding.get()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = MainFrame(master=root)
    app.mainloop()







#Calculations


#Output GUI
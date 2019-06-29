import tkinter
import pandas
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *


#User Input and Input GUI

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

        self.shares_outstanding_text = ttk.Label(text='Shares Outstanding (Millions): ')
        self.shares_outstanding_text.grid(column=1,row=1)

        self.shares_outstanding = tk.Entry()
        self.shares_outstanding.grid(column=2,row=1)

        self.rrf_text = ttk.Label(text='Risk Free Rate (%): ')
        self.rrf_text.grid(column=1,row=2)

        self.rrf = tk.Entry()
        self.rrf.grid(column=2,row=2)

        self.beta_text = ttk.Label(text='Beta: ')  
        self.beta_text.grid(column=1,row=3)

        self.beta = tk.Entry()
        self.beta.grid(column=2,row=3)

        self.mrp_text = ttk.Label(text='Current Equity Risk Premium: ')
        self.mrp_text.grid(column=1,row=4)

        self.mrp = tk.Entry()
        self.mrp.grid(column=2,row=4)

        self.fcfe_text = ttk.Label(text='Initial Free Cash Flow to Equity: ')  
        self.fcfe_text.grid(column=1,row=5)

        self.fcfe = tk.Entry()
        self.fcfe.grid(column=2,row=5)

        self.five_year_gr_text = ttk.Label(text='Five Year Growth Rate (%): ')  
        self.five_year_gr_text.grid(column=1,row=6)

        self.five_year_gr = tk.Entry()
        self.five_year_gr.grid(column=2,row=6)

        self.terminal_gr_text = ttk.Label(text='Terminal Growth Rate (%): ')
        self.terminal_gr_text.grid(column=1,row=7)

        self.terminal_gr = tk.Entry()
        self.terminal_gr.grid(column=2,row=7)
#revise below and add oher variables

        self.label_pps = tk.Label(text="default text")
        self.label_pps.grid(column=3,row=0)
    

        self.label_shares_outstanding = tk.Label(text="default text")
        self.label_shares_outstanding.grid(column=3,row=1)

        self.button1 = ttk.Button(text='confirm inputs', command=self.write)
        self.button1.grid(column=1,row=9)

    def write(self):
        #self.label_pps["text"]=self.pps.get()
        #self.label_shares_outstanding["text"]=self.shares_outstanding.get()
        pps = self.pps.get()
        shares_outstanding = self.shares_outstanding.get()
        rrf = self.rrf.get()
        beta = self.beta.get()
        mrp = self.mrp.get()
        fcfe = self.fcfe.get()
        five_year_gr = self.five_year_gr.get()
        terminal_gr = self.terminal_gr.get()
        
        


if __name__ == "__main__":
    root = tk.Tk()
    app = MainFrame(master=root)
    app.mainloop()


#Calculations
cost_of_equity = rrf + beta * mrp

fcfe_y1 = (fcfe*(1+five_year_gr))/((1+cost_of_equity)**1)
fcfe_y2 = (fcfe*(1+five_year_gr)**2)/((1+cost_of_equity)**2)
fcfe_y3 = (fcfe*(1+five_year_gr)**3)/((1+cost_of_equity)**3)
fcfe_y4 = (fcfe*(1+five_year_gr)**4)/((1+cost_of_equity)**4)
fcfe_y5 = (fcfe*(1+five_year_gr)**5)/((1+cost_of_equity)**5)

five_year_value = fcfe_y1 + fcfe_y2 + fcfe_y3 + fcfe_y4 + fcfe_y5

terminal_value = (fcfe*(1+five_year_gr)**5)/((cost_of_equity-terminal_gr)*(1+cost_of_equity)**5







#Output GUI
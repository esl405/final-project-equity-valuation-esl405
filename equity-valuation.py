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

        self.five_year_gr_text = ttk.Label(text='Five Year Growth Rate (As Decimal): ')  
        self.five_year_gr_text.grid(column=1,row=6)

        self.five_year_gr = tk.Entry()
        self.five_year_gr.grid(column=2,row=6)

        self.terminal_gr_text = ttk.Label(text='Terminal Growth Rate (As Decimal): ')
        self.terminal_gr_text.grid(column=1,row=7)

        self.terminal_gr = tk.Entry()
        self.terminal_gr.grid(column=2,row=7)

#added confirmation test
        self.header_text = ttk.Label(text='Confirmation Inputs: ')  
        self.header_text.grid(column=3,row=0)
        
        self.label_shares_outstanding = tk.Label(text="default text")
        self.label_shares_outstanding.grid(column=3,row=1)

        self.label_rrf = tk.Label(text="default text")
        self.label_rrf.grid(column=3,row=2)

        self.button1 = ttk.Button(text='Confirm Inputs', command=self.write)
        self.button1.grid(column=1,row=9)

        self.button2 = ttk.Button(text='Close Window', command= quit)
        self.button2.grid(column=2,row=9)

    def write(self):
        self.label_shares_outstanding["text"]=self.shares_outstanding.get()
        self.label_rrf["text"]=self.rrf.get()
        pps = float(self.pps.get())
        shares_outstanding = float(self.shares_outstanding.get())
        rrf = float(self.rrf.get())
        beta = float(self.beta.get())
        mrp = float(self.mrp.get())
        fcfe = float(self.fcfe.get())
        five_year_gr =float(self.five_year_gr.get())
        terminal_gr = float(self.terminal_gr.get())
        #Calculations
        cost_of_equity = rrf + beta * mrp

        fcfe_y1 = (fcfe*(1+five_year_gr))/((1+cost_of_equity)**1)
        fcfe_y2 = (fcfe*(1+five_year_gr)**2)/((1+cost_of_equity)**2)
        fcfe_y3 = (fcfe*(1+five_year_gr)**3)/((1+cost_of_equity)**3)
        fcfe_y4 = (fcfe*(1+five_year_gr)**4)/((1+cost_of_equity)**4)
        fcfe_y5 = (fcfe*(1+five_year_gr)**5)/((1+cost_of_equity)**5)

        five_year_value = fcfe_y1 + fcfe_y2 + fcfe_y3 + fcfe_y4 + fcfe_y5
        terminal_value = (fcfe*(1+terminal_gr)*(1+five_year_gr)**5)/((cost_of_equity-terminal_gr)*(1+cost_of_equity)**5)
        equity_value = five_year_value + terminal_value
        value_per_share = equity_value / shares_outstanding
        premium_discount = pps / value_per_share

        five_year_value_USD= '${0:.2f}'.format(five_year_value)
        terminal_value_USD= '${0:.2f}'.format(terminal_value)
        equity_value_USD= '${0:.2f}'.format(equity_value)
        value_per_share_USD= '${0:.2f}'.format(value_per_share)
        premium_discount_short = '{0:.2f}'.format(premium_discount)
        #to test outputs only
        #print(terminal_value) 
        #print(equity_value)
        #print(value_per_share)
        #print(premium_discount)
        
        #Output GUI Window
        root=Tk()
        root.title("Equity Valulation: ")
        root.geometry("300x200")
        Label(root, text='Cost of Equity: ').grid(row=1, column=1)
        Label(root, text=cost_of_equity).grid(row=1, column=2)
        Label(root, text='Five Year Value ($M): ').grid(row=2, column=1)
        Label(root, text=five_year_value_USD).grid(row=2, column=2)
        Label(root, text='Terminal Value ($M): ').grid(row=3, column=1)
        Label(root, text=terminal_value_USD).grid(row=3, column=2)
        Label(root, text='NPV Equity Value ($M): ').grid(row=4, column=1)
        Label(root, text=equity_value_USD).grid(row=4, column=2)
        Label(root, text='PPS ($): ').grid(row=5, column=1)
        Label(root, text=pps).grid(row=5, column=2)
        Label(root, text='Value Per Share ($): ').grid(row=6, column=1)
        Label(root, text=value_per_share_USD).grid(row=6, column=2)
        Label(root, text='Premium/Discount: ').grid(row=7, column=1)
        Label(root, text=premium_discount_short).grid(row=7, column=2)
        Button(root, text='Quit',command=quit, fg='red').grid(row=8, column=1)
        root.mainloop()

    #def new_window():
    #    root=Tk()
    #    root.title("Equity Valulation: ")
    #    root.geometry("500x500")
    #    Label(root, text='Cost of Equity: ').grid(row=1, column=1)
    #    Label(root, text=cost_of_equity).grid(row=1, column=2)
    #    #Button(root, text='Quit',command=quit, fg='red').pack(side=LEFT)
    #    root.mainloop()
  
    
if __name__ == "__main__":
    root = tk.Tk()
    app = MainFrame(master=root)
    app.mainloop()
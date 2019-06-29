#from https://www.sololearn.com/Discuss/501434/need-example-for-get-values-from-textbox-tkinter
import tkinter as tk
from tkinter import ttk

class MainFrame(ttk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()

        
        
    def create_widgets(self):
        
        self.textbox1 = tk.Entry()
        self.textbox1.grid(column=2,row=0)

        
        self.button1 = ttk.Button(text='put entry box text on label', command=self.write)
        self.button1.grid(column=1,row=0)

        self.textbox2 = tk.Entry()
        self.textbox2.grid(column=2,row=1)

        
        self.button1 = ttk.Button(text='put entry box text on label', command=self.write)
        self.button1.grid(column=1,row=1)


        self.label1 = tk.Label(text="default text")
        self.label1.grid(column=3,row=0)

        self.label2 = tk.Label(text="default text")
        self.label2.grid(column=3,row=1)

    def write(self):
        self.label1["text"]=self.textbox1.get()
        self.label2["text"]=self.textbox2.get()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = MainFrame(master=root)
    app.mainloop()

#Calculation Test

pps = 134.20
shares_outstanding = 7660
rrf = 0.0237
beta = 1.29
mrp = 0.0538
fcfe = 29519
five_year_gr = 0.0245
terminal_gr = 0.0230

cost_of_equity = rrf + beta * mrp

fcfe_y1 = (fcfe*(1+five_year_gr))/((1+cost_of_equity)**1)
fcfe_y2 = (fcfe*(1+five_year_gr)**2)/((1+cost_of_equity)**2)
fcfe_y3 = (fcfe*(1+five_year_gr)**3)/((1+cost_of_equity)**3)
fcfe_y4 = (fcfe*(1+five_year_gr)**4)/((1+cost_of_equity)**4)
fcfe_y5 = (fcfe*(1+five_year_gr)**5)/((1+cost_of_equity)**5)

five_year_value = fcfe_y1 + fcfe_y2 + fcfe_y3 + fcfe_y4 + fcfe_y5

terminal_value = (fcfe*(1+five_year_gr)**5)/((cost_of_equity-terminal_gr)*(1+cost_of_equity)**5)

equity_value = five_year_value + terminal_value

value_per_share = equity_value / shares_outstanding

premium_discount = pps / value_per_share


print(five_year_value)
print(terminal_value)
print(equity_value)
print(value_per_share)
print(premium_discount)
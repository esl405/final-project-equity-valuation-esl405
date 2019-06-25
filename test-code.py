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
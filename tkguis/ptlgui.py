import tkinter as tk
from math import ceil
from decimal import Decimal

def roundup(x, factor):
    return (ceil(Decimal(x) * Decimal(factor)))/Decimal('100')

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        #self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.label1 = tk.Label(text="orig").grid(row=0, column=0)
        
        self.entryx = tk.Entry()
        #self.entryx.pack()
        self.entryx.grid(row=0, column=1)
        self.entryx.bind('<Key-Return>', self.say_hi)
        self.entryx.bind('<Button-1>', self.clearall)

        self.label2 = tk.Label(text="20%").grid(row=1, column=0)
        self.twenty = tk.Entry()
        #self.twenty.pack()
        self.twenty.grid(row=1, column=1)

        self.label3 = tk.Label(text="21%").grid(row=2, column=0)
        self.twentyone = tk.Entry()
        #self.twentyone.pack()
        self.twentyone.grid(row=2, column=1)

        self.label4 = tk.Label(text="22%").grid(row=3, column=0)
        self.twentytwo = tk.Entry()
        #self.twentytwo.pack()
        self.twentytwo.grid(row=3, column=1)

        self.all = tk.Entry(width=26)
        #self.all.pack()
        self.all.grid(row=4, column=0, columnspan=2)

        #self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        #self.QUIT.pack(side="bottom")

    def clearall(self, event):
        self.twenty.delete(0, len(self.twenty.get()))
        self.twentyone.delete(0, len(self.twentyone.get()))
        self.twentytwo.delete(0, len(self.twentytwo.get()))
        self.all.delete(0, len(self.all.get()))
        self.entryx.delete(0, len(self.entryx.get()))
        
    def say_hi(self, event):
        x = self.entryx.get()
        x = x.replace(",", ".")

        #self.entryx.delete(0, len(self.entryx.get()))
        
        self.twenty.delete(0, len(self.twenty.get()))
        self.twenty.insert(0, '{0:.2f}'.format(roundup(x, '240')))

        self.twentyone.delete(0, len(self.twentyone.get()))
        self.twentyone.insert(0, '{0:.2f}'.format(roundup(x, '237')))

        self.twentytwo.delete(0, len(self.twentytwo.get()))
        self.twentytwo.insert(0, '{0:.2f}'.format(roundup(x, '234')))

        fl = float(x)

        self.all.delete(0, len(self.all.get()))
        self.all.insert(0, '{:.2f}, {:.4f}, {:.4f}, {:.4f}'.format(fl, fl * 2.4, fl * 2.37, fl * 2.34))


root = tk.Tk()
app = Application(master=root)
app.mainloop()

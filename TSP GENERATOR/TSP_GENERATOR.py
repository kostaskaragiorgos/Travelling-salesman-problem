"""
generates tsp instances
"""
from tkinter import Label, Text, Button, Tk, Menu, IntVar, Radiobutton
from tkinter import filedialog, END
from tkinter import simpledialog
from tkinter import messagebox as msg
import random as rd
import  numpy as np
def helpmenu():
    """ help menu function """
    msg.showinfo("HELP", "ENTER THE NUMBER OF NODES PICK ONE OF THE WAYS TO CREATE THE NODES AND PRESS GENERATE")
def aboutmenu():
    """ about menu function """
    msg.showinfo("About", "Version 1.0")
def values_bounds(self):
    """ user sets the range of distance """
    self.startingvalue = simpledialog.askinteger("Min Distance", "Enter the value of the min possible distance", parent=self.master, minvalue=1)
    while self.startingvalue is None:
        self.startingvalue = simpledialog.askinteger("Min Distance", "Enter the value of the min possible distance", parent=self.master, minvalue=1)
    self.endingvalue = simpledialog.askinteger("Max Distance", "Enter the max possible distance", parent=self.master, minvalue=self.startingvalue+1)
    while self.endingvalue is None:
        self.endingvalue = simpledialog.askinteger("Max Distance", "Enter the max possible distance", parent=self.master, minvalue=self.startingvalue+1)
    return self.startingvalue, self.endingvalue
def asymmetric_table(self):
    """ creaton of asymmetric table """
    a = np.ones((int(self.text.get(1.0, END)), int(self.text.get(1.0, END))))
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                a[[i], [j]] = 0
            elif i > j:
                a[[i], [j]] = rd.randint(self.startingvalue, self.endingvalue)
            else:
                a[[i], [j]] = rd.randint(self.startingvalue, self.endingvalue)
    return a
def symmetric_table(self):
    """ creates a symmetric table """
    a = np.ones((int(self.text.get(1.0, END)), int(self.text.get(1.0, END))))
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                a[[i], [j]] = 0
            elif i > j:
                a[[i], [j]] = rd.randint(self.startingvalue, self.endingvalue)
    for i in range(len(a)):
        for j in range(len(a)):
            if i < j:
                a[[i], [j]] = a[[j], [i]]
    return a
def save_file(a):
    """ saves .txt file """
    filenamesave = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    if ".txt" in filenamesave:
        np.savetxt(filenamesave, a, fmt ='%1d', delimiter=' ')
        msg.showinfo("Success", "Success")
    else:
        msg.showerror("Abort", "Abort")
class TSP_GENERATOR():
    """
    TSP_GENERATOR class
    """
    def __init__(self, master):
        self.master = master
        self.master.title("TSP-GENERATOR")
        self.master.geometry("190x150")
        self.master.resizable(False, False)
        self.leb = Label(self.master, text="Enter the number of nodes")
        self.leb.pack()
        self.text = Text(self.master, height=1, width=3)
        self.text.pack()
        self.r = IntVar()
        self.r.set(1)
        self.totrand = Radiobutton(self.master, text="ASYMMETRIC", variable=self.r, value=2)
        self.totrand.pack()
        self.back_and_forth = Radiobutton(self.master, text="SYMMETRIC", variable=self.r, value=1)
        self.back_and_forth.pack()
        self.geb = Button(self.master, text="GENERATE", command=self.gen)
        self.geb.pack()
        #menu
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Generate", accelerator='Ctrl+O',command=self.gen)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-o>', lambda event: self.gen())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        self.master.bind('<Control-o>', lambda  event: self.gen()) 
    def exitmenu(self):
        """ exit menu function """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    def gen(self):
        """ generates the instance and saves it to a .txt file"""
        try:
            if int(self.text.get(1.0, END)) >= 4:
                values_bounds(self)
                if self.r.get() == 1:
                    a = symmetric_table(self)
                elif self.r.get() == 2:
                    a = asymmetric_table(self)
                save_file(a)
            else:
                msg.showerror("Value Error", "Enter a number higher than four")
        except:
            msg.showerror("Value Error", "Enter a number higher than four")
            self.text.delete(1.0, END)    
def main():
    """ main function"""
    root = Tk()
    TSP_GENERATOR(root)
    root.mainloop()
if __name__ == '__main__':
    main()
from tkinter import Label, Text, Button, Tk, Menu, IntVar, Radiobutton
from tkinter import filedialog , END
from tkinter import simpledialog
from tkinter import messagebox as msg
import  numpy as np
import random as rd
import pandas as pd
def helpmenu():
    msg.showinfo("HELP","ENTER THE NUMBER OF NODES PICK ONE OF THE WAYS TO CREATE THE NODES AND PRESS GENERATE")
def aboutmenu():
    msg.showinfo("About","Version 1.0")
class TSP_GENERATOR ():
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
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu,tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        self.master.bind('<Control-o>', lambda  event: self.gen()) 
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    def gen(self):
        """ generates the instance and saves it to a .txt file"""
        self.startingvalue = simpledialog.askinteger("Min Distance", "Enter the value of the min possible distance", parent=self.master, minvalue=1)
        while self.startingvalue is None:
            self.startingvalue = simpledialog.askinteger("Min Distance", "Enter the value of the min possible distance", parent=self.master, minvalue=1)
        self.endingvalue = simpledialog.askinteger("Max Distance", "Enter the max possible distance", parent=self.master, minvalue=self.startingvalue+1)
        while self.endingvalue is None:
            self.endingvalue = simpledialog.askinteger("Max Distance", "Enter the max possible distance", parent=self.master, minvalue=self.startingvalue+1)
        create_table = 0
        try:
            if int(self.text.get(1.0, END)) >= 4:
                create_table += 1
            else:
                msg.showerror("Value Error", "Enter a number higher than four")
        except:
            msg.showerror("Value Error", "Enter a number higher than four")
            self.text.delete(1.0, END)
            create_table = 0
        
        if create_table == 1:
            if self.r.get() == 1:
                a =  np.ones((int(self.text.get(1.0, END)), int(self.text.get(1.0, END))))
                for i in range(len(a)):
                    for j in range(len(a)):
                        if i == j:
                            a[[i], [j]] = 0
                        elif i>j:
                            a[[i], [j]] = rd.randint(self.startingvalue, self.endingvalue)
                for i in range(len(a)):
                    for j in range(len (a)):
                        if i<j:
                            a[[i], [j]] = a[[j], [i]]
            elif self.r.get() == 2:
                a =  np.ones((int(self.text.get(1.0, END)), int(self.text.get(1.0, END))))
                for i in range(len(a)):
                    for j in range(len(a)):
                        if i == j:
                            a[[i], [j]] = 0
                        elif i>j:
                            a[[i], [j]] = rd.randint(self.startingvalue, self.endingvalue)
                for i in range(len(a)):
                    for j in range(len (a)):
                        if i<j :
                            a[[i], [j]] = rd.randint(self.startingvalue, self.endingvalue)
            filenamesave =  filedialog.asksaveasfilename(initialdir = "/", title = "Select file", filetypes = (("txt files", "*.txt"), ("all files", "*.*")))
            if ".txt" in filenamesave:
                with open(filenamesave, 'w') as f:
                    for i in range(len(a)):
                        for j in range(len(a)):
                            f.write(str(a[i][j])+" ")
                        f.write("\n")
                msg.showinfo("Success", "Success")
            else:
                msg.showerror("Abort" , "Abort")
def main():
    root = Tk()
    TSP_GENERATOR(root)
    root.mainloop()
if __name__ == '__main__':
    main()
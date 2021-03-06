""" tsp solver """
from tkinter import Tk, Menu, OptionMenu, Button, StringVar, Label, Text, END
from tkinter import messagebox as msg
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from algorithms.nearestneighbor import nearserN
from algorithms.fileparser import fileparser
from algorithms.relocate import relocatef
from algorithms.swap import swap
from algorithms._2_opt import _2optf
def helpmenu():
    """ help menu function """
    msg.showinfo("Help", "A TSP SOLVER")
def aboutmenu():
    """ about menu function """
    msg.showinfo("About", "Version 1.0")
class TSP_SOLVER2():
    """ tsp solver class"""
    def __init__(self, master):
        self.master = master
        self.master.title("TSP_SOLVER 2")
        self.master.geometry("250x200")
        self.master.resizable(False, False)
        self.filed = ""
        # menu 
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Insert a file", accelerator='Ctrl+O', command=self.insertfile)
        self.file_menu.add_command(label="Solve",
                                   accelerator='Alt+F5', command=self.solve)
        self.file_menu.add_command(label="Close file", accelerator="Ctrl+F5", command=self.cf)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.show_menu = Menu(self.menu, tearoff=0)
        self.show_menu.add_command(label='Instance Plot', command=self.instanceplot)
        self.menu.add_cascade(label='Show', menu=self.show_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Control-o>', lambda event: self.insertfile())
        self.master.bind('<Alt-F5>', lambda event: self.solve())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        self.master.bind('<Control-F5>', lambda event: self.cf())
        self.binsert = Button(self.master, text="Insert a file", command=self.insertfile)
        self.binsert.pack()
        setslist = list(["2-opt", "Relocate", "Swap"])
        self.varnumset = StringVar(master)
        self.varnumset.set(setslist[0])
        self.popupsetmenu = OptionMenu(self.master, self.varnumset, *setslist)
        self.popupsetmenu.pack()
        self.lb = Label(self.master, text="TRIES")
        self.lb.pack()
        self.textt = Text(self.master, height=1)
        self.textt.pack()
    def exitmenu(self):
        """ exit menu function """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    def instanceplot(self):
        """ plots the instance"""
        if self.filed == "":
            msg.showerror("ERROR", "NO FILE IMPORTED TO PLOT")
        else:
            data = np.loadtxt(self.filed)
            x = data[:, 0]
            y = data[:, 1]
            plt.scatter(x, y)
            plt.show()
    def cf(self):
        """ closes the file """ 
        if self.filed == "":
            msg.showerror("NO FILE", "NO FILE TO CLOSE")
        else:
            self.filed = ""
            self.popupsetmenu.forget()
            self.solvb.forget()
            msg.showinfo("FILE CLOSED", "SUCCESS") #CHANGE THE MESSAGE 
    def file_verification_gui(self):
        """ gui created after file verification"""
        self.nodelist = list(self.number)
        self.varnumnode = StringVar(self.master)
        self.varnumnode.set(self.nodelist[0])
        self.popupsetmenu = OptionMenu(self.master, self.varnumnode, *self.nodelist)
        self.popupsetmenu.pack()
        self.solvb = Button(self.master, text="Solve", command=self.solve)
        self.solvb.pack()
    def file_verification(self):
        try:
            self.table, self.number = fileparser(self.filed)
            self.file_verification_gui()
            msg.showinfo("SUCCESS", "THE FILE SUCCESSFULLY INSERTED \nNumber of nodes:" + str(len(self.number)))
        except ValueError:
            msg.showerror("ERROR", "NO TSP INSTANCE INSERTED")
            self.filed = ""

    def checkinsertedfiletype(self):
        if ".txt" in self.filed:
            self.file_verification()
        else:
            msg.showerror("Error", "NO TXT FILE ADDED")
    def insertfile(self):
        """ user inserts a .txt file (problem instance ) """
        if self.filed == "":
            self.filed = filedialog.askopenfilename(initialdir="/", title="Select txt file",
                                                    filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
            self.checkinsertedfiletype()
        else:
            msg.showerror("ERROR", "YOU NEED TO CLOSE THE FILE")
    def algouse(self, tries, visited_nodes, totalscore):
        if self.varnumset.get() == "2-opt":
            current_route, current_score = _2optf(visited_nodes, totalscore, tries, self.table, self.number)
        elif self.varnumset.get() == "Relocate":
            current_route, current_score = relocatef(visited_nodes, totalscore, tries, self.table, self.number)
        else:
            current_route, current_score = swap(visited_nodes, totalscore, tries, self.table, self.number)
        msg.showinfo("SUCCESS", "THE ROUTE USING "+self.varnumset.get()+" :"+str(current_route)+"WITH SCORE:"+str(current_score))
        self.textt.delete(1.0, END)
    def check_tries(self, visited_nodes, totalscore):
        try:
            if int(self.textt.get(1.0, END)) > 0:
                self.algouse(int(self.textt.get(1.0, END)), visited_nodes, totalscore)
            else:
                msg.showerror("Value Error", "Enter a number higher than zero")
                self.textt.delete(1.0, END)
        except ValueError:
            msg.showerror("Value Error", "Enter a number higher than zero")
            self.textt.delete(1.0, END)
    def solve(self):
        """ solves the problem """
        if self.filed == "":
            msg.showinfo("Import", "You need to import a .txt file")
        else:
            visited_nodes, totalscore = nearserN(self.table, self.number, self.varnumnode.get())
            self.check_tries(visited_nodes, totalscore)
def main():
    """ main function """
    root = Tk()
    TSP_SOLVER2(root)
    root.mainloop()
if __name__ == '__main__':
    main()

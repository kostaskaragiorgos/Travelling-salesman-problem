""" TSP SOLVER """
from tkinter import Menu, Button, StringVar, OptionMenu, messagebox as msg, filedialog, Tk
import numpy as np
import matplotlib.pyplot as plt
from algorithms.nearestneighbor import nearserN
from algorithms.fileparser import fileparser

def helpmenu():
    """ help menu """
    msg.showinfo("Help", "A TSP SOLVER")
    
def aboutmenu():
    """ about menu """
    msg.showinfo("About", "Version 1.0")

class TSP_SOLVER():
    """ TSP SOLVER CLASS """
    def __init__(self, master):
        self.master = master
        self.master.title("TSP_SOLVER")
        self.master.geometry("250x120")
        self.master.resizable(False, False)
        self.filed = ""

        #menu
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Insert a file", accelerator='Ctrl+O', command=self.insertfile)
        self.file_menu.add_command(label="Solve", accelerator='Alt+F5', command=self.solve)
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
        self.master.bind('<Control-F5>', lambda event: self.cf())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        
        self.binsert = Button(self.master, text="Insert a file", command=self.insertfile)
        self.binsert.pack()

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
        """ closes the .txt file """
        if self.filed == "":
            msg.showerror("ERROR", "NO FILE IMPORTED TO CLOSE")
        else:
            self.filed = ""
            self.popupsetmenu.forget()
            self.solvb.forget()
            msg.showinfo("SUCCESS", "FILE CLOSED")
    def exitmenu(self):
        """ exit """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def file_verification_gui(self):
        nodelist = list(self.number)
        self.varnumnode = StringVar(self.master)
        self.varnumnode.set(nodelist[0])
        self.popupsetmenu = OptionMenu(self.master, self.varnumnode, *nodelist)
        self.popupsetmenu.pack()

        self.solvb = Button(self.master, text="Solve", command=self.solve)
        self.solvb.pack()

    def insertfile(self):
        """ user inserts a .txt file (problem instance ) """
        if self.filed == "":
            self.filed = filedialog.askopenfilename(initialdir="/", title="Select txt file",
                                                    filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
          
            if ".txt" in self.filed:
                try:
                    self.table, self.number = fileparser(self.filed)
                    self.file_verification_gui()
                    msg.showinfo("SUCCESS", "THE FILE SUCCESSFULLY INSERTED \nNumber of nodes:" + str(len(self.number)))
                except ValueError:
                    msg.showerror("ERROR", "NO TSP INSTANCE INSERTED")
                    self.filed = ""
            else:
                msg.showerror("Error", "NO TXT FILE ADDED")
        else:
            msg.showerror("ERROR", "YOU NEED TO CLOSE THE FILE")
                

    def solve(self):
        """ solves the problem """
        if self.filed == "":
            msg.showinfo("Import", "You need to import a .txt file")
        else:
            visited_nodes, totalscore = nearserN(self.table, self.number, self.varnumnode.get()) 
            msg.showinfo("SUCCESS", "THE ROUTE USING NEAREST NEIGHBOR"+str(visited_nodes)+"with score:"+str(totalscore))
    
def main():
    """ main function """
    root = Tk()
    TSP_SOLVER(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()

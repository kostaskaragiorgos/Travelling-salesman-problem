from tkinter import Tk, Menu, Button, Label, Text, OptionMenu, StringVar, END
from tkinter import messagebox as msg
from tkinter import filedialog
from nearestneighbor import *
from _2_opt import partial_reverse, _2optf
from basicvn import bvns
from relocate import *
def helpmenu():
    """ help menu"""
    msg.showinfo("Help", "A TSP SOLVER")
def aboutmenu():
    """ about menu"""
    msg.showinfo("About", "Version 1.0")
class TSP_META_SOLVER():
    """ tsp meta solver """
    def __init__(self, master):
        self.master = master
        self.master.title("TSP_META_SOLVER")
        self.master.geometry("250x130")
        self.master.resizable(False, False)
        self.filed = ""
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Insert a file", accelerator='Ctrl+O', command=self.insertfile)
        self.file_menu.add_command(label="Solve", accelerator='Alt+F5', command=self.solve)
        self.file_menu.add_command(label="Close file", accelerator="Ctrl+F5", command=self.cf)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
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
        self.master.bind('<Control-F5>', lambda event: self.cf())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        self.binsert = Button(self.master, text="Insert a file", command=self.insertfile)
        self.binsert.pack()
        self.lb = Label(self.master, text="TRIES")
        self.lb.pack()
        self.textt = Text(self.master, height=1)
        self.textt.pack()
    def cf(self):
        """ close file"""
        if self.filed == "":
            msg.showerror("ERROR", "NO FILE IMPORTED TO CLOSE")
        else:
            self.filed = ""
            self.popupsetmenu.forget()
            self.solvb.forget()
            msg.showinfo("SUCCESS", "FILE CLOSED")
    def exitmenu(self):
        """ exit menu function """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    def insertfile(self):
        """ insert file function """
        if self.filed == "":
            self.filed = filedialog.askopenfilename(initialdir="/", title="Select txt file",
                                                    filetypes=(("txt files", "*.txt"),
                                                               ("all files", "*.*")))
            if ".txt" in self.filed:
                self.table, self.number = fileparser(self.filed)
                nodelist = list(self.number)
                self.varnumnode = StringVar(self.master)
                self.varnumnode.set(nodelist[0])
                self.popupsetmenu = OptionMenu(self.master, self.varnumnode, *nodelist)
                self.popupsetmenu.pack()
                self.solvb = Button(self.master, text="Solve", command=self.solve)
                self.solvb.pack()
            else:
                msg.showerror("Error", "NO TXT FILE ADDED")
        else:
            msg.showerror("ERROR", "YOU NEED TO CLOSE THE FILE")
    def solve(self):
        """ solve Button function """
        if self.filed == "":
            msg.showinfo("Import", "You need to import a .txt file")
        else:
            visited_nodes, totalscore = nearserN(self.table, self.number, self.varnumnode.get()) 
            try:
                if int(self.textt.get(1.0, END)) > 0:
                    tries = int(self.textt.get(1.0, END))
                    lista = [relocatef(visited_nodes, totalscore, tries, self.table, self.number), _2optf(visited_nodes, totalscore, tries, self.table, self.number)]
                    new_route, new_score = bvns(visited_nodes, totalscore, lista, tries)
                    msg.showinfo("Total Score", "Route:"+str(new_route)+ "Score:"+str(new_score))
                    self.textt.delete(1.0, END)
                else:
                    msg.showerror("Value Error", "Enter a number higher than zero")
                    self.textt.delete(1.0, END)
            except ValueError:
                msg.showerror("Value Error", "Enter a number higher than zero")
                self.textt.delete(1.0, END)
def main():
    """ main function"""
    root = Tk()
    TSP_META_SOLVER(root)
    root.mainloop()
if __name__ == '__main__':
    main()

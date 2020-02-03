from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog
from nearestneighbor import *
import pandas as pd 
import numpy as np
class TSP_SOLVER ():
    
    def __init__(self,master):
        self.master = master
        self.master.title("TSP_SOLVER")
        self.master.geometry("250x120")
        self.master.resizable(False,False)
        self.filed = ""

        #menu
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Insert a file",accelerator = 'Ctrl+O',command = self.insertfile)
        self.file_menu.add_command(label = "Solve",accelerator = 'Alt+F5',command = self.solve)
        self.file_menu.add_command(label = "Close file",accelerator = "Ctrl+F5",command = self.cf)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Control-o>',lambda event:self.insertfile())
        self.master.bind('<Alt-F5>',lambda event:self.solve())
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F5>',lambda event: self.cf())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
        
        self.binsert = Button(self.master,text = "Insert a file",command = self.insertfile)
        self.binsert.pack()
    
    def cf(self):
        if self.filed == "":
            msg.showerror("ERROR", "NO FILE IMPORTED TO CLOSE")
        else:
            self.filed = ""
            msg.showinfo("SUCCESS", "FILE CLOSED")

    
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    
    
    def insertfile(self):
        """ user inserts a .txt file (problem instance ) """

        self.filed = filedialog.askopenfilename(initialdir="/",title="Select txt file",
                                                   filetypes=(("txt files","*.txt"),("all files","*.*")))
          
        if ".txt" in self.filed:
            self.table,self.number = fileparser(self.filed)
            nodelist = list(self.number)
            self.varnumnode = StringVar(self.master)
            self.varnumnode.set(nodelist[0])
            self.popupsetmenu = OptionMenu(self.master,self.varnumnode,*nodelist)
            self.popupsetmenu.pack()
            
            self.solvb = Button(self.master,text = "Solve",command = self.solve)
            self.solvb.pack()
        else:
            msg.showerror("Error","NO TXT FILE ADDED")
                
    def helpmenu(self):
        msg.showinfo("Help","A TSP SOLVER")
    
    def aboutmenu(self):
        msg.showinfo("About","Version 1.0")
        


    def solve(self):
        if self.filed  == "":
            msg.showinfo("Import", "You need to import a .txt file")
        else:
            visited_nodes, totalscore = nearserN(self.table,self.number,self.varnumnode.get()) 
            msg.showinfo("SUCCESS", "THE ROUTE USING NEAREST NEIGHBOR"+str(visited_nodes)+"with score:"+str(totalscore))

        
    
def main():
    root=Tk()
    TSP_S = TSP_SOLVER(root)
    root.mainloop()
    
if __name__=='__main__':
    main()

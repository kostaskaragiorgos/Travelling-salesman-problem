from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog
from nearestneighbor import *
from _2_opt import partial_reverse, _2optf
from swap import swap ,swapPositions
from relocate import *
import pandas as pd 
import numpy as np
class TSP_SOLVER2 ():
    
    def __init__(self,master):
        self.master = master
        self.master.title("TSP_SOLVER 2")
        self.master.geometry("250x160")
        self.master.resizable(False,False)
        self.filed = ""
        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Insert a file",accelerator = 'Ctrl+O',command = self.insertfile)
        self.file_menu.add_command(label = "Solve",accelerator = 'Alt+F5',command = self.solve)
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
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
        
        self.binsert = Button(self.master,text = "Insert a file",command = self.insertfile)
        self.binsert.pack()

        setslist = list(["2-opt","Relocate","Swap"])
        self.varnumset = StringVar(master)
        self.varnumset.set(setslist[0])
        self.popupsetmenu = OptionMenu(self.master,self.varnumset,*setslist)
        self.popupsetmenu.pack()
        
        self.lb = Label(self.master,text = "TRIES")
        self.lb.pack()

        self.textt = Text(self.master , height = 1)
        self.textt.pack()

    
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    
    
    def insertfile(self):

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
            try:
                if int(self.textt.get(1.0,END)) > 0:
                    tries = int(self.textt.get(1.0,END))

                    if self.varnumset.get() == "2-opt":
                        current_route , current_score  = _2optf(visited_nodes , totalscore , tries,self.table,self.number)
                        msg.showinfo("SUCCESS", "THE ROUTE USING 2-OPT:"+str(current_route)+"WITH SCORE:"+str(current_score))
                        self.textt.delete(1.0,END)
                    elif self.varnumset.get() == "Relocate":
                        current_route , current_score  =relocatef(visited_nodes , totalscore , tries,self.table,self.number)
                        msg.showinfo("SUCCESS", "THE ROUTE USING RELOCATE :"+str(current_route)+"WITH SCORE:"+str(current_score))
                        self.textt.delete(1.0,END)
                    else:
                        current_route , current_score  =swap(visited_nodes , totalscore , tries,self.table,self.number)
                        msg.showinfo("SUCCESS", "THE ROUTE USING SWAP :"+str(current_route)+"WITH SCORE:"+str(current_score))
                        self.textt.delete(1.0,END)

                else:
                    msg.showerror("Value Error", "Enter a number higher than zero")
                    self.textt.delete(1.0,END)
            except:
                msg.showerror("Value Error", "Enter a number higher than zero")
                self.textt.delete(1.0,END)


        

def main():
    root=Tk()
    TSP_S = TSP_SOLVER2(root)
    root.mainloop()
    
if __name__=='__main__':
    main()

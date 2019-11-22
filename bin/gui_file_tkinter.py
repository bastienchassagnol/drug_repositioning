# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:20:12 2019

@author: Bastien
"""
import tkinter as tk
from tkinter import filedialog

 
class GUI_get_file():
    def __init__(self, master):
        self.master=master
        master.title("Folder window")
        master.geometry("600x600")
        self.dirname=None
        self.filename_list=[]
        self.listbox = tk.Listbox(master,  width=100)
        self.listbox.pack(side=tk.TOP)
         
        self.bouton_getfiles = tk.Button(master, text="Get Files", command=self.GetFiles)
        self.bouton_getfiles.pack(side=tk.LEFT)
         
        self.bouton_getdir = tk.Button(master, text="Get Dir", command=self.GetDir)
        self.bouton_getdir.pack(side=tk.LEFT)
         
        self.delete_button = tk.Button(master, text="Delete",command=self.DeleteSelection)
        self.delete_button.pack(side=tk.LEFT)
        
        
    def AddFilelistbox(self,filename):
        if (filename):
            self.listbox.insert(tk.END, filename)
           
    
    def AddFolderlistbox(self,dirname):
        if (dirname):
            self.listbox.insert(tk.END, dirname)
         
    def DeleteSelection(self) :
        items = self.listbox.curselection()
        pos = 0
        for i in items :
            idx = int(i) - pos
            self.listbox.delete( idx,idx )
            pos = pos + 1
     
    def GetFiles(self):
        filename = filedialog.askopenfilename(defaultextension='.per', filetypes=[('All files','*.*')])
        self.filename_list.append(filename)
        self.AddFilelistbox(filename)
     
    def GetDir(self):
        dirname = filedialog.askdirectory()
        self.dirname=dirname
        self.AddFilelistbox(dirname)
            
       
        
            
        
if __name__ == '__main__':
    master=tk.Tk()
    GE=GUI_get_file(master)
    master.mainloop()    
    print("\n***** after tkinter exits, entered =", GE.dirname)









 
 

     









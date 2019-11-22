# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:17:36 2019

@author: Bastien
"""

import tkinter as tk
from gui_file_tkinter import GUI_get_file
import re

def GUI_get_foldername():
    master=tk.Tk()
    folder_path_window=GUI_get_file(master)
    master.mainloop()    
    if folder_path_window.dirname:
        return folder_path_window.dirname
    else:
        raise ValueError("Folder name is empty")
        
        
def replace_string_file(path_file, old_terms,new_terms):
    with open(path_file, 'r') as file :
      filedata = file.read()
      for (old_element, new_element) in zip (old_terms,new_terms):
        filedata=filedata.replace(old_element,new_element)
    with open(path_file, 'w') as file:
      file.write(filedata)
      
def replace_with_regular_expression(path_file, old_terms,new_terms):
    with open(path_file, 'r') as file :
      filedata = file.read()
      for (old_element, new_element) in zip (old_terms,new_terms):
        filedata=re.sub(old_element,new_element,filedata)
    with open(path_file, 'w') as file:
      file.write(filedata)
    
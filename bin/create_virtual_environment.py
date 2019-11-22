# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:05:04 2019

@author: Bastien
"""

import os
import re
from miscelleanous_functions import GUI_get_foldername
import platform



#verify and download requirements
os.system ('cmd /c " pip install --upgrade --user virtualenv"')
#get folder where to build virtual environment and use it
folder_target_path=GUI_get_foldername()

#ask folder name, allowing only alpha_numeric or underscores characters
folder_name = input("Enter folder's name of your virtual environment, with only underscores and alpha_numeric characters : ") 
path_env_project_name=os.path.join(folder_target_path,folder_name)
if re.match('^[a-zA-Z0-9_]+$',folder_name):    
    os.system ("virtualenv "+path_env_project_name)
else:
    raise ValueError("Your folder includes forbidden characters")
    
#activation file is not the same according we are on linux or Windows
if platform.system()=="Windows":
    os.system(os.path.join(path_env_project_name, "Scripts\activate.bat"))
else:
    os.system("source "+os.path.join(path_env_project_name, "bin/activate"))

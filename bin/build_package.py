# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:30:02 2019

@author: Bastien
"""

#for each command to be done separetely, use a &
import os, subprocess, shlex
from miscelleanous_functions import replace_string_file


#ask where to launch all the commands (parent file of the package)
from miscelleanous_functions import GUI_get_foldername
package_path=GUI_get_foldername()

#get tot he parent repository of the package
print( "package path chosen is {} .".format(package_path))
os.chdir (package_path)
#verify and download requirements
print(subprocess.run (shlex.split("pip install --upgrade setuptools twine pip wheel virtualenv sphinx pytest"), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True))

#to install the documentation we first check if docs folder is present, launch sphinx command and then return to parent directory

if not os.path.exists("docs"):
    os.makedirs('docs')

print(subprocess.run(shlex.split("sphinx-quickstart --ext-autodoc --quiet --sep -p patrimony_computationnal_platform -a bastienchassagnol -v 0.1 -l e"),stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,cwd=os.path.join(os.getcwd(),"docs")))
replace_string_file(os.path.join(os.getcwd(),"docs","source","conf.py"), ["# import os", "# import sys", "# sys.path.insert(0, os.path.abspath('.'))"], ["import os", "import sys", "sys.path.append(0, os.path.abspath({}))".format(package_path)])
print(subprocess.run(shlex.split("make html"),stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,cwd=os.path.join(os.getcwd(),"docs")))
                    
#test all files containing test as well as print included for debbuging by first creating th conf file, and then modify it as required


print(subprocess.run(shlex.split("pytest","-s"),stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,text=True))

#remove cache that might lead to error computations and build package (binary and minimal version) 

print(subprocess.run((shlex.split("rm -rf dist build */*.egg-info *.egg-info & python setup.py bdist_wheel sdist")),stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True))


"""
#verify and download requirements
os.system ('cmd /c " pip install --upgrade setuptools twine pip wheel venv sphinx pytest"')

os.system('cmd /c " cd docs & sphinx-quickstart"')
os.system ('cmd /c " cd .."')

os.chdir('docs')
os.system('cmd /K sphinx-quickstart')
#test all files containing test as well as print included for debbuging
os.system('cmd /c " pytest -s "')

#remove cache that might lead to error computations and build package (binary and minimal version) 
os.system('cmd /c "rm -rf dist build */*.egg-info *.egg-info  & python setup.py bdist_wheel sdist"')

#install package locally (better to perform it on virtual environment) in local and editable mode
#os.system('cmd /c " pip install -e ."') #(optionnal)

#send package on testPypi, the test repository website for Python package 
#os.system ('cmd /c " twine --repository-url https://test.pypi.org/legacy/ upload dist/*" ')

#send package on Pypi, the official repository website for Python package 
#os.system ('cmd /c " twine upload dist/*" ')

#to install package from Pypi, as a remote test
#os.system ('cmd /c " pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-bastienchassagnol"')

"""
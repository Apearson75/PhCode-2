import argparse
import re
import os
import json
from lib.changeVar import changeB

from lib.send import sendB
from lib.var import varB

print("Remember to download Pyinstaller using  pip install -U pyinstaller\n\n")

#Args
parser = argparse.ArgumentParser(description='loads .ph file')
parser.add_argument(
    '-l',
    '--load',
    type=str,
    help='Enter the name of the .ph file.'
)
args = parser.parse_args()
file_path = args.load
file = open(file_path, 'r')
lines = file.readlines()

count = 0
variables = {}
py_file = ""


export = input("Export to exe (Y/n) ")

for line in lines:
    count += 1
    operation = line.split(" ")[0]

    #Check for \n
    if line == "\n":
        py_file = py_file + "\n"

    #Check for '#'
    elif line[0] == "#":
        py_file = py_file + line    
    
    #Print Command
    elif operation == "send":
        py_file += sendB(line)

    #Variable Command
    elif operation == "var":    
        py_file += varB(line, variables)
    
    #End Command
    elif operation == "end" or operation == "end\n":
        py_file = py_file + 'input("Press Enter to Finish ")\n'
        py_file = py_file + "raise SystemExit\n"    

    #Changing variables
    else:
        py_file += changeB(line, variables)



#Add data to out.py 
try:    
    with open("out.py", "x") as out:
        out.write(py_file) 
except:
    with open("out.py", "w") as w:
        w.write(py_file)               

if export == "y" or export == "Y":
    os.system("pyinstaller --onefile out.py")
    os.system("rmdir /s /q build")
    input("\n\nExported to Exe")

else:
    input("\n\nExported to out.py")
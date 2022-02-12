import argparse
import re
import os
import json

print("Remember to download Nuitka using  pip install -U nuitka\n\n")

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
    if line[0] == "#":
        py_file = py_file + line    
    
    #Print Command
    if operation == "send":
        if '"' not in line:
            result = line.split("send ")[1]
            result_name = result.replace("\n", "")
            py_file = py_file + f"print({result_name})\n"
        else:        
            result = line.split("send ")[1]
            result = re.search('"(.*)"', result)
            py_file = py_file + f"print('{result.group(1)}')\n"

    #Variable Command
    elif operation == "var":    
        variable = line.split("var ")[1]
        variable_name = variable.split(" ")[0]
        variable_data = variable.split(f"{variable_name} ")[1]
        print(variable_data)
        variables[variable_name] = variable_data
        json.dumps(variables)
        py_file = py_file + f"{variable_name} = {variable_data}\n"
    
    #End Command
    elif operation == "end" or operation == "end\n":
        py_file = py_file + 'input("Press Enter to Finish ")\n'
        py_file = py_file + "raise SystemExit\n"    

try:    
    with open("out.py", "x") as out:
        out.write(py_file) 
except:
    with open("out.py", "w") as w:
        w.write(py_file)               

if export == "y" or export == "Y":
    os.system("nuitka --standalone out.py")
    print("\n\nExported to Exe")
    input("")

else:
    print("\n\nExported to out.py")
    input("")
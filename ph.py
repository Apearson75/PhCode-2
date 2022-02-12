from pprint import pprint
import re
import json
import sys
import argparse

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

#Operator check for variables
operators = ['send', 'var', 'is', 'end']

#Get the file
file = open(file_path, 'r')
lines = file.readlines()

#For the lines and stuff
count = 0
variables = {}

for line in lines:
    count += 1
    operation = line.split(" ")[0]
    
    #Check for '#'
    if line[0] == "#":
        pass 

    #Check for \n
    elif line == "\n":
        pass
    
    #Print Command
    elif operation == "send":
        if '"' not in line:
            result = line.split("send ")[1]
            result = result.replace("\n", "")
            result = variables[result]
            result = re.search('"(.*)"', result)
            print(result.group(1))
        else:    
            try:    
                result = line.split("send ")[1]
                result = re.search('"(.*)"', result)
                print(result.group(1))
            except AttributeError:
                print(f"String Error in line {count} on {file.name}")
    
    #Variable Command
    elif operation == "var":    
        variable = line.split("var ")[1]
        variable_name = variable.split(" ")[0]
        variable_data = variable.split(f"{variable_name} ")[1]

            
        variables[variable_name] = variable_data
        json.dumps(variables)
        

    #Is Command
    elif operation == "is":
        result = line.split("is ")[1]
        if eval(result):
            print(True)
        else:
            print(False)       
    
    
    #End Command
    elif operation == "end" or operation == "end\n":
        input("\n\nPress Enter to Finish ")
        raise SystemExit

    #Changing variables
    else:
        variable_name = line.split(" ")[0]
        variable_data = line.split(f"{variable_name} ")[1]
        if variable_name in variables:
            variables[variable_name] = variable_data

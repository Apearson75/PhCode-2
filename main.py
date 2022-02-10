from pprint import pprint
import re
import json

#Operator check for variables
operators = ['send', 'var']

#Get the file
file = input("Type the name of your file you want to run")
if file == "":
    file = "main.ph"
file = open(file, 'r')
lines = file.readlines()

#For the lines and stuff
count = 0
variables = {}

for line in lines:
    count += 1
    operation = line.split(" ")[0]
    
    #Print Command
    if operation == "send":
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
import json

def change(line, variables):
    variable_name = line.split(" ")[0]
    variable_data = line.split(f"{variable_name} ")[1]
    if variable_name in variables:
        variables[variable_name] = variable_data

def changeB(line, variables):
    variable_name = line.split(" ")[0]
    variable_data = line.split(f"{variable_name} ")[1]
    if variable_name in variables:
        variables[variable_name] = variable_data
        json.dumps(variables)
        py_file = f"{variable_name} = {variable_data}"
        return py_file        
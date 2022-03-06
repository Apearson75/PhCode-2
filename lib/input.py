import re
import json

def Input(line : str):
    result = line.split("input ")[1]
    result = re.search('"(.*)"', result)
    input(result.group(1))

def InputV(variables, variable_data, variable_name):
    input_data = variable_data.split("input ")[1]
    input_data = input_data.replace('"', '')
    variables[variable_name] = input(input_data)
    json.dumps(variables)   
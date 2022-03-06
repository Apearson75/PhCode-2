import re

def send(line, variables):
    if '"' not in line:
            result = line.split("send ")[1]
            result = result.replace("\n", "")
            result = variables[result]
            result = re.search('"(.*)"', result)
            print(result.group(1))
    else:        
        result = line.split("send ")[1]
        result = re.search('"(.*)"', result)
        print(result.group(1))

def sendB(line):
    if '"' not in line:
        result = line.split("send ")[1]
        result_name = result.replace("\n", "")
        py_file = f"print({result_name})\n"
        return py_file
    else:        
        result = line.split("send ")[1]
        result = re.search('"(.*)"', result)
        py_file = f"print('{result.group(1)}')\n"
        return py_file        
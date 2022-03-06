import re

def Input(line : str):
    result = line.split("input ")[1]
    result = re.search('"(.*)"', result)
    input(result.group(1))
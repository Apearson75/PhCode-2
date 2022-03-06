from pprint import pprint
import re
import json
import sys
import argparse
from lib.IS import IS
from lib.changeVar import change
from lib.input import Input

from lib.send import send
from lib.var import var

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
operators = ['send', 'var', 'is', 'end', 'input']

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
        send(line, variables)
    
    #Variable Command
    elif operation == "var":    
        var(line, variables)
        

    #Is Command
    elif operation == "is":
        IS(line)

    #Input Command
    elif operation == "input":
        Input(line)    
    
    #End Command
    elif operation == "end" or operation == "end\n":
        input("\n\nPress Enter to Finish ")
        raise SystemExit

    #Changing variables
    else:
        change(line, variables)

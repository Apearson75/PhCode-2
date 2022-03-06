def IS(line):
    result = line.split("is ")[1]
    if eval(result):
        print(True)
    else:
        print(False)       
    